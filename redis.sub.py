# coding=utf-8
__author__ = 'JIE'

import redis
r = redis.StrictRedis()

p = r.pubsub()
p.subscribe("channel")
for message in p.listen():
    print(message)

print(p.get_message())
