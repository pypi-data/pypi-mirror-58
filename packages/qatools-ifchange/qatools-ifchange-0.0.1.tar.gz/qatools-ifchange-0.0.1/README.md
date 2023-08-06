## 介绍说明
相似问平台主要由Question Analysis、Retrieval、Matching、Rank等部分组成，其中包含的功能均通过插件形式加入，如Analysis中的中文切词，Retrieval中的倒排索引、语义索引，Matching中的Jaccard特征、语义匹配特征等，SimQP的配置化、插件化设计有助于开发者快速构建、快速定制适用于特定业务场景的FAQ相似问检索系统，加速迭代和升级。 结构如下图：![](https://gitlab.ifchange.com/nlu/SimQP/raw/dev/docs/images/SimQP_Framework.png)

### 快速启动
- 启动服务： python server/start_qa_server.py
- 测试请求：curl -i -X POST -H 'Content-type':'application/json' -d '{"traffic_paramsDict":{"query":"五险一金相关的规定"}}' 127.0.0.1:54321/qaservice

### 配置化
相似问平台集成了检索和匹配的众多插件，通过配置的方式生效；以检索方式和文本匹配相似度计算中的插件为例：
- 检索方式(Retrieval)
    - 倒排索引：基于terms的字段，建立倒排索引solr
    - 语义检索：基于语义表示，建立向量索引
    - 人工干预：通过提供精准答案，控制输出
- 匹配计算(Matching)
    - 字面匹配相似度：在对中文问题进行切词等处理之后，计算字面匹配特征
        - Cosine相似度
        - BM25
    - 语义匹配相似度：构建问题对在语义层面的特征
        - KNRM
### 插件化
所有功能都是通过插件形式加入，用户自定义的插件很容易加到平台中，只需实现对应的接口即可。

## 目录结构
```
.  
├── README.md  
├── conf  # 配置文件 
│   └── simqp.yaml  
├── data  
│   ├── embedding.txt  # 词向量
│   ├── prefix.txt     # 前缀
│   ├── punction.txt   # 标点
│   ├── samples.txt    # 语料库
│   ├── stopwords.txt  # 停用词
│   ├── suffix.txt     # 后缀
│   ├── synonym.txt    # 同义词
│   └── user_dict.txt  # 用户字典 
├── docs  
│   └── config_tutorial.md  
├── server  
└── src  
    ├── analysis  # 分析模块
    │   ├── analysis_base.py  
    │   ├── analysis_strategy.py  
    │   ├── dataclean.py  
    │   ├── senemb.py  
    │   └── wordseg.py  
    ├── common    # 工具模块
    │   ├── load_dataset.py  
    │   ├── logger.py  
    │   └── utils.py  
    ├── dict      # 字典管理模块
    │   └── dict_manager.py  
    ├── matching  # 匹配模块
    │   ├── lexical  
    │   ├── matching_base.py  
    │   ├── matching_strategy.py  
    │   └── senmantic  
    ├── rank      # 排序模块
    │   ├── predictor  
    │   ├── rank_base.py  
    │   └── rank_strategy.py  
    ├── retrieval  # 召回模块 
    │   ├── manual  
    │   ├── retireval_base.py  
    │   ├── retrieval_strategy.py  
    │   ├── senmantic  
    │   └── term  
    ├── server     # 服务模块 
    └── simqp_strategy.py   # 主函数
  
18 directories, 27 files  
```
