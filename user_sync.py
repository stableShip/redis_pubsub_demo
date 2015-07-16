# coding=utf-8
__author__ = 'JIE'

import redis

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        r = redis.StrictRedis()
        while True:
            openid = r.brpop("usersync")
            if openid:
                print(openid)


def test():
    t = MyThread()
    t.start()


if __name__ == '__main__':
    test()


def exec_sync(mapping, id):
    pass