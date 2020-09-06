import redis
import random
from collections import Counter

cli = redis.StrictRedis(host="localhost", port=6379, decode_responses=True, db=0)
pre = ['', '', '']
length = 200
i = 0
while i < length:
    print(pre[0], end='')
    t = pre
    surfixes = cli.lrange("('%s', '%s', '%s')" % (pre[0], pre[1], pre[2]), 0, -1)
    pre[0] = t[1]
    pre[1] = t[2]
    pre[2] = random.choice(surfixes)
    i += 1
