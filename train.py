import jieba
import json
import os
import nltk
import redis
import time

src = ''

def train(fn):
    with open(fn, 'r', encoding='UTF-8') as f:
        text = f.read().replace('\n', '')

    time_start = time.time()
    words = jieba.lcut(text)
    four_grams = nltk.ngrams(words, 4)
    time_end = time.time()
    print('四元组分组完成，开始配置数据库。用时：', str(time_end-time_start))


    time_start = time.time()
    conn = redis.StrictRedis(host="localhost", port=6379, decode_responses=True, db=0)
    print('数据库配置完成，开始训练模型。用时：', str(time_end-time_start))

    time_start = time.time()
    for i in four_grams:
        pre = "('%s', '%s', '%s')" % (i[0], i[1], i[2])
        conn.rpush(pre, i[3])
    time_end = time.time()
    print('模型训练完成。用时：', str(time_end-time_start))

os.chdir(src)
files = os.listdir(src)
total = len(files)
for i in range(total):
    fn = 'wiki_' + str(i)
    print('正在训练：', fn)
    train(fn)
    print('该文件训练完成，进度：{:.2%}'.format((i+1)/total))
