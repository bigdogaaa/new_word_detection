import os
import WordTool

project_dir = os.path.dirname(WordTool.__file__)

import pandas as pd
from utils.convert_tw2zh import convert_tw2zh_opencc

pd.set_option('display.max_rows', None)

static_set = set()

for line in open(project_dir+'/static/现代汉语常用词表.txt', 'r', encoding='utf-8'):
    parts = line.split('\t')
    static_set.add(parts[0])


def filter_with_dic(word_list):
    result = []
    for w in word_list:
        if w not in static_set:
            result.append(w)
    return result





