__author__ = 'rahul'

import redis
from ..config import libconf


def init_app(app):
    redisd = redis.StrictRedis(host=libconf.REDIS_HOST, port=libconf.REDIS_PORT, db=libconf.DB_INDEX)
    pubsubd = redisd.pubsub()
    pubsubd.subscribe(libconf.EMAIL_Q)

    return redisd, pubsubd