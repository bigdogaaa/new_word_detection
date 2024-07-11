import pandas as pd
from utils.convert_tw2zh import convert_tw2zh_opencc

pd.set_option('display.max_rows', None)

static_set = set()

for line in open('D:\数据集\话语体系/现代汉语常用词表.txt', 'r', encoding='utf-8'):
    parts = line.split('\t')
    static_set.add(parts[0])


df = pd.read_csv('./new_word_detection_result.csv')
print(df)
for index, item in df.iterrows():
    w = item['w']
    w = convert_tw2zh_opencc(w)
    if w not in static_set:
        print(w)

