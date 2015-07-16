# coding=utf-8
__author__ = 'JIE'
import redis

r = redis.StrictRedis()
# r.set("test", 3)

r.publish("channel", "test2")
