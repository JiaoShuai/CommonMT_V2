import csv
import json

# CSV文件路径
csv_file = 'lexical_ambiguity.csv'

# 输出的JSONL文件路径
jsonl_file = 'lexical_ambiguity.jsonl'

import csv
import json

import csv
import jsonlines

# CSV文件路径

# 输出的JSONL文件路径

# 读取CSV文件并转换为JSONL格式
with open(csv_file, mode='r', encoding='utf-8') as csv_file, \
        open(jsonl_file, mode='w', encoding='utf-8') as jsonl_file:
    
    csv_reader = csv.DictReader(csv_file)
    jsonl_writer = jsonlines.Writer(jsonl_file)
    
    for row in csv_reader:
        jsonl_writer.write(row)

# 注意 jsonlines.Writer 会自动处理文件的开头和结尾，所以不需要手动添加开头和结尾标记

