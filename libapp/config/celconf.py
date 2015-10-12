__author__ = 'leena'


from libapp.config import libconf

# Celery configuration
BROKER_URL = "redis://{rserver}:{rport}/{rdb}".format(rserver=libconf.REDIS_HOST, rport=libconf.REDIS_PORT, rdb=libconf.DB_INDEX)
CELERY_RESULT_BACKEND = "redis://"
BROKER_TRANSPORT = 'redis'

CELERY_BROKER_HOST = "redis://{rserver}:{rport}".format(rserver=libconf.REDIS_HOST, rport=libconf.REDIS_PORT)