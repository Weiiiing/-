# 成语构词大模型的数字人文应用
- 训练成语构词大模型用于领域知识重组、回溯与发现，文章信息：
- 张卫，王东波，刘浏. 基于大语言模型的成语隐喻式构词方法及其应用：知识重组、回溯与发现. **_情报学报_** (2025).

## 1. 成语构词大模型
- 定义基于<短语结构，物象标签（源域），情感标签（目标域）>三元组的成语隐喻式构词知识体系，以成语出处文本为输入，成语构词结构为输出，立足句法特征探索Prompt模板设计与问答学习语料建设策略；引入荀子生成式大模型进行短语抽取、隐喻识别多任务联合建模，重点验证依存句法知识注入下构词大模型指令微调的增强效果；结合结构与内容层面的评价指标对大模型生成的构词结构进行多元评估。

## 2. File
- "Hownet" is the China HowNet emotional dictionary.
- "NTUSD" is the National Taiwan University sentiment lexicon.
- "Li Jun lexicon" is the Li Jun sentiment lexicon of Tsinghua University.
- "DUTIR" is the ontology database of emotion vocabulary of the Dalian University of Technology.
- "FCCPSL" is the constructed poetry sentiment lexicon.
- "Appreciation Dictionary of Tang Poetry" is the experimental corpus.

## 3. Methods and results
### 3.1 Sentiment term extraction
A list of multi-source sentiment words is collected from the general sentiment vocabularies and related domains to form the knowledge base. Next, the sentiment words are used to match the terms in the domain text, and the annotated text is then mapped to a character labeling sequence. Next, the BERT model is used to realize Chinese character embedding, after which the emotion radical (ER) features of Chinese characters are incorporated to extend the BERT vector to boost semantic information. The enhanced vector is input into a neural network to predict the labels of sequences to extract sentiment terms. The extracted terms include domain terms in the original vocabularies and unregistered terms predicted by the model. The results are as follows:
