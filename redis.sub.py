# coding=utf-8
__author__ = 'JIE'

import redis

r = redis.StrictRedis()
r.config_set("notify-keyspace-events", "KEA")
p = r.pubsub()
# p.
p.subscribe("__keyspace@0__:test")
for message in p.listen():
    print(message)

print(p.get_message())

