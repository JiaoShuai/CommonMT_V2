import sacrebleu
 
# 参考翻译
references = [['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.']]
 
# 机器翻译结果
hypothesis = 'The dog bit the man.'
 
# 计算 BLEU 分数
score = sacrebleu.corpus_bleu([hypothesis], references)
 
print(score)
