__author__ = 'leena'

import json

import redis
from config.publisher_config import get_msg
from libapp import celeryd, pubsubd
from config import libconf as settings


queue = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.DB_INDEX)
# channel = queue.pubsub()

# sender = settings.SENDER
# recipient = settings.RECIPIENT


def test():
    msg = get_msg(settings.SENDER, settings.RECIPIENT)
    queue.publish(settings.EMAIL_Q, json.dumps(msg))


@celeryd.task()
def publish_msg():
    data = queue.lpop(settings.EMAIL_Q + '-pub')
    # d = json.loads(data)
    # sender = d.get("sender", settings.SENDER)
    # recipient = d.get("recipient", settings.RECIPIENT)
    # msg = get_msg(sender, recipient)
    queue.publish(settings.EMAIL_Q, data)
