__author__ = 'rahul'

import redis
from ..config import libconf as settings


def init_app(app):
    redisd = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.DB_INDEX)
    pubsubd = redisd.pubsub()
    pubsubd.subscribe(settings.EMAIL_Q)

    return redisd, pubsubd