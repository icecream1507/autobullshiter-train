import jieba
import json
import nltk
import redis
import time

src = ''

with open(src, 'r', encoding='UTF-8') as f:
    text = f.read()

time_start = time.time()
words = jieba.lcut(text)
#bigrams = nltk.bigrams(words)
trgrams = nltk.ngrams(words, 3)
time_end = time.time()
print('三元组分组完成，开始配置数据库。用时：', str(time_end-time_start))


time_start = time.time()
conn = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)
print('数据库配置完成，开始训练模型。用时：', str(time_end-time_start))

time_start = time.time()
for t in trgrams:
    pre = "('%s', '%s')" % (t[0], t[1])
    conn.rpush(pre, t[2])
    print(conn.lrange(pre, 0, -1))
time_end = time.time()
print('模型训练完成。用时：', str(time_end-time_start))

print("完成")
