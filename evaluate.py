import sacrebleu
# "After school, these students agreed to go to the reservoir together for swimming."
# 参考翻译（可以有多个参考句子）
references = [
    ["After school, these students agreed to go to the reservoir together for swimming.",]
]
# 候选翻译
hypothesis = ["After school, these students had planned to go swimming at the reservoir."]
# 计算 BLEU 分数
score = sacrebleu.corpus_bleu(hypothesis, references)
print(score)

# 计算 chrF++
score = sacrebleu.corpus_chrf(hypothesis, references)
print(score)
