import redis
import random
from collections import Counter

cli = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)
pre = ['', '']
length = 0
i = 0
while i < length:
    print(pre[0], end='')
    surfixes = cli.lrange("('%s', '%s')" % (pre[0], pre[1]), 0, -1)
    word_counts = Counter(surfixes)
    pre[0] = pre[1]
    choices = word_counts.most_common(2)
    pre[1] = random.choice(choices)[0]
    i += 1