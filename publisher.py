__author__ = 'leena'

import json

import redis
from config.publisher_config import get_msg
from config import library as settings


queue = redis.StrictRedis(host=settings.HOST, port=settings.PORT, db=settings.DB_INDEX)
channel = queue.pubsub()

sender = settings.SENDER
recipient = settings.RECIPIENT

msg = get_msg(sender, recipient)
queue.publish(settings.EMAIL_Q, json.dumps(msg))
