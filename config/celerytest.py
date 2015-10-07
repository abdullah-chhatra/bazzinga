__author__ = 'leena'


from config.library import (REDIS_HOST, REDIS_PORT, DB_INDEX)

# Celery configuration
BROKER_URL = "redis://{rserver}:{rport}/{rdb}".format(rserver=REDIS_HOST, rport=REDIS_PORT, rdb=DB_INDEX)
CELERY_RESULT_BACKEND = "redis://"
BROKER_TRANSPORT = 'redis'

CELERY_BROKER_HOST = "redis://{rserver}:{rport}".format(rserver=REDIS_HOST, rport=REDIS_PORT)