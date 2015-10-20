__author__ = 'leena'


from libapp.config import libconf

# Celery configuration
# Custom
CELERY_LOG_LEVEL = "WARNING"
CELERY_CONCURRENCY = 1

# Original
CELERY_TIMEZONE = "Asia/Kolkata"

# Optimization configurations
CELERY_ACKS_LATE = True
CELERY_PREFETCH_MULTIPLIER = 1
CELERY_ACCEPT_CONTENT = ['json']

#Broker configurations
BROKER_TRANSPORT = "redis"
BROKER_URL = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                            rport=libconf.REDIS_PORT, rdb=libconf.DB_INDEX)
CELERY_RESULT_BACKEND = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT,
                                                                       rserver=libconf.REDIS_HOST,
                                                                       rport=libconf.REDIS_PORT, rdb=libconf.DB_INDEX)

CELERY_BROKER_HOST = "{transport}://{rserver}:{rport}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                              rport=libconf.REDIS_PORT)