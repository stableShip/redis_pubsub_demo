# coding=utf-8
__author__ = 'JIE'
import redis

r = redis.StrictRedis()
r.set("test2", 123)
r.publish("channel", "test2")
