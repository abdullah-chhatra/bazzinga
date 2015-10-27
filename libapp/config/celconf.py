__author__ = 'leena'

from datetime import timedelta
from libapp.config import libconf

# Celery configuration
# Custom
# "INFO"
CELERY_LOG_LEVEL = "WARNING"
CELERY_LOG_FILE = "celery.log"
CELERY_CONCURRENCY = 1

# Original
CELERY_TIMEZONE = "Asia/Kolkata"

# Optimization configurations
CELERY_ACKS_LATE = True
CELERY_PREFETCH_MULTIPLIER = 1
CELERY_ACCEPT_CONTENT = ["json"]

# Scheduler
CELERYBEAT_SCHEDULE = {
    "add-every-10-seconds": {
        "task": "libapp.subscriber.subscribe_data",
        "schedule": timedelta(seconds=10),
        #"args": (16, 16)
        "options": {
            "queue" : libconf.EMAIL_Q,
            "serializer" : "json"
        }
    },
}

#Broker configurations
BROKER_TRANSPORT = "redis"
BROKER_URL = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                            rport=libconf.REDIS_PORT, rdb=libconf.DB_INDEX)
CELERY_RESULT_BACKEND = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT,
                                                                       rserver=libconf.REDIS_HOST,
                                                                       rport=libconf.REDIS_PORT, rdb=libconf.DB_INDEX)

CELERY_BROKER_HOST = "{transport}://{rserver}:{rport}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                              rport=libconf.REDIS_PORT)