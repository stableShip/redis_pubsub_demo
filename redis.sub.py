# coding=utf-8
__author__ = 'JIE'

import redis

r = redis.StrictRedis()
p = r.pubsub()

def user_sync(message):
    openid = bytes.decode(message['data'])
    print (r.get(openid))


p.subscribe(**{"channel": user_sync})
p.run_in_thread()
