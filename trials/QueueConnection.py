import os
import redis
import threading
from flask import Flask, render_template
from flask import Response
from flask import json
import pickle
import time

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = r.pubsub()


class Listener(threading.Thread):

    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    def work(self, item):
        print item['channel'], ":", item['data']

    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print self, "unsubscribed and finished"
                break
            else:
                self.work(item)

if __name__ == "__main__":
    client = Listener(r, ['emails'])
    client.start()
    for i in range(10):
        r.publish("hello", i)
        time.sleep(0.5)
    r.publish('test11', 'this will reach the listener')
    r.publish('fail', 'this will not')
    r.publish('test12', 'KILL')


