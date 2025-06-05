### The Box is in the Pen: Evaluating Commonsense Reasoning in Neural Machine Translation
***
This is the official repo for the Findings of EMNLP 2020 paper: [The Box is in the Pen: Evaluating Commonsense Reasoning in Neural Machine Translation](https://www.aclweb.org/anthology/2020.findings-emnlp.327/) .

This repository contains three types of test suite:

*  lexical ambiguity

*  contextless syntactic ambiguity

*  contextual syntactic ambiguity

#### Data License

Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.
(License URL: https://creativecommons.org/licenses/by-sa/4.0/)


翻译

The Box is in the Pen:Evaluating Commonsense Reasoning in Neural Machine Translation

---

这是 EMNLP 2020 论文《The Box is in the Pen:Evaluating Commonsense Reasoning in Neural Machine Translation》的官方代码仓库：[The Box is in the Pen:Evaluating Commonsense Reasoning in Neural Machine Translation]()。

这个代码仓库包含三种类型的测试套件：


• 词汇歧义

• 无上下文的句法歧义

• 有上下文的句法歧义


数据许可
署名-相同方式共享 4.0 国际(CC BY-SA 4.0)许可证。
(许可证 URL:[]())



# CommonMT_V2
A refined CommonMT test suite

删掉了源数据集的"(好像第二个是对的）"

听了他安慰的话，一股暖流涌上心头。(好像第二个是对的）,"After listening to his words for comfort, a warm emotion came to my heart.","After listening to his words for comfort, a warm current rushed into my heart."

## lexical_ambiguity.jsonl 文件格式
```json
{"chinese_source": "他想拉同村的干部一起下水去贩毒。", "english_target_correct": "He wants to take the cadres of the same village to sell drugs with him.", "english_target_wrong": "He wants to pull the cadres of the same village to enter the water to sell drugs."}


```
## contextual_syntactic_ambiguity.jsonl 文件格式 
```json
{"chinese_source": "当地震袭击中国时，援助的是中国。", "english_target_correct": "When the earthquake hit China, China was aided.", "english_target_wrong": "When the earthquake hit China,  China has assisted."}

```

## contextless_syntactic_ambiguity.jsonl 文件格式

```json
{"chinese_source": "发明的是一个伟大的科学家。 ", "english_target_correct": "A great scientist invented it.", "english_target_wrong": "A great scitentist was invented."}
``` 
