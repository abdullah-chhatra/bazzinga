__author__ = 'leena'

import redis
import time
import pickle
import json

queue = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = queue.pubsub()

sender = "hello@mycuteoffice.com"
receiver =  ["leenakhote23@gmail.com" ,"khoteleena5@gmail.com"]
author = "space_provider"
category = "space_progress"
subject = "space_progress"


def get_value(subject):
       return { "Status of Booking ID: Accepted" : {"name" : "leena" ,"space_id" :"12345" ,"book_id" : "34"} ,
                "enquiry_reply" :{"name" : "hello" , "date" : "12345678"},
                "space_progress" : {"name" : "zebu"}
       }[subject]


msg1 = {"sender": sender, "recipient": receiver, "author": author, "category": category,
        "subject": subject, "email_content": get_value(subject)}

queue.publish('lee', json.dumps(msg1))
