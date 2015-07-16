# coding=utf-8
__author__ = 'JIE'
import redis
r = redis.StrictRedis()
print (r.config_get("notify-keyspace-events"))
# r.config_set("notify-keyspace-events", "KEA")
r.set("test", 3)

r.publish("channel", "test2")
