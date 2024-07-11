import pandas as pd
from WordTool import WordTool
from utils.preprocess import clean_text
from tqdm import tqdm
import pickle as pkl
import os

dp = 'D:\话语体系模型\数据集\新闻网站/'
fn = '纽约时报中文.csv'

if not os.path.exists('./wordtool.pkl'):
    df = pd.read_csv(dp + fn, encoding='utf-8').iloc[:500]
    content = []
    for index, item in tqdm(df.iterrows()):
        text = item['content']
        text = clean_text(text)
        content.append(text)

    w = WordTool(content)
else:
    w = pkl.load(open('./wordtool.pkl', 'r', encoding='utf-8'))
# Step 1
# 输入最大词长d，生成所有可能的单词组合。结果见w.pool
w.setPool(d=5)
# Step 2
# 为上一部生成的候选词统计词频
w.countPool()
# Step 3
# 设置最小词频，从pool中筛选出候选词。结果见w.candidates
w.setCandidates(min_freq=5)
# Step 4
# 计算w.candidates中候选词左右邻字的信息熵。会更新w.candidates
w.setCandidatesEntropy()
# Step 5
# 计算w.candidates中候选词的凝聚度。会更新w.candidates
w.setCondensity()

df = w.display(sort="condensity",  # 按照设定属性从大到小排序，可选condensity,freq,entropy_left,entropy_right
               min_freq=0,
               min_entropy_left=1.3,
               min_entropy_right=1.3,
               min_condensity=100,
               user_dict=None,  # 如果给定额外词典，则只展示额外词典中不存在的新词
               )

df.to_csv('./new_word_detection_result.csv', encoding='utf-8')
print(df)

# w.display方法会将筛选结果更新到w.data中，方便后续处理
