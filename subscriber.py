__author__ = 'leena'

import redis
import time
import pickle
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('lee')


def subscribe_data():
    while True:
        message = p.get_message()
        if message:
            data = message.get('data')
            print("Subscriber: %s" % data)
            if type(data) is not long and data:
                category = json.loads(data)['category']
                author = json.loads(data)['author']
                sender = json.loads(data)['sender']
                receiver1 = json.loads(data)['receiver']
                receiver = "leenakhote23@gmail.com"
                print category , author , sender , receiver

    return category ,author , sender , receiver