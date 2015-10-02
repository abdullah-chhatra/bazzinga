__author__ = 'leena'

import redis
import time
import pickle
import json

queue = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = queue.pubsub()

msg = {"sender" : "hello@mycuteoffice.com", "receiver" : ["leenakhote23@gmail.com" ,"khoteleena5@gmail.com"],
       "author" : "space_seeker", "category": "feedback_system"}
queue.publish('lee', json.dumps(msg))
