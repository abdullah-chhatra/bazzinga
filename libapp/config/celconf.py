__author__ = 'leena'

from datetime import timedelta
from . import libconf

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

# Scheduler celery config
PUBLISHER_QS = [libconf.PUB_EMAIL_Q, libconf.PUB_SMS_Q, libconf.PUB_PUSH_Q]
SUBSCRIBER_QS = [libconf.EMAIL_Q, libconf.SMS_Q, libconf.PUSH_Q]

# Scheduler
CELERYBEAT_SCHEDULE = {
    "add-email-every-5-seconds": {
        "task": "libapp.tasks.transform_data",
        "schedule": timedelta(seconds=5),
        "args": (PUBLISHER_QS, SUBSCRIBER_QS),
        "options": {
            "queue" : libconf.EMAIL_Q,
            "serializer" : "json"
        }
    },

    "add-email-every-2-seconds": {
        "task": "libapp.tasks.subscribe_data",
        "schedule": timedelta(seconds=2),
        #"args": (16, 16)
        "options": {
            "queue" : libconf.EMAIL_Q,
            "serializer" : "json"
        }
    },
}

# Broker dbs
BROKER_DB = 0
BACKEND_DB = 1

#Broker configurations
BROKER_TRANSPORT = "redis"
BROKER_URL = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                            rport=libconf.REDIS_PORT, rdb=BROKER_DB)
CELERY_RESULT_BACKEND = "{transport}://{rserver}:{rport}/{rdb}".format(transport=BROKER_TRANSPORT,
                                                                       rserver=libconf.REDIS_HOST,
                                                                       rport=libconf.REDIS_PORT, rdb=BACKEND_DB)

CELERY_BROKER_HOST = "{transport}://{rserver}:{rport}".format(transport=BROKER_TRANSPORT, rserver=libconf.REDIS_HOST,
                                                              rport=libconf.REDIS_PORT)