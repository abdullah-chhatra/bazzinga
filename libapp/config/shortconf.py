# Redis configurations
SHORTNER_HOST = "localhost"
SHORTNER_PORT = 6379
# DB List
SHORTNER_DB = 2

SHORTNER_STORE = "redis"
SHORTNER_CLIENT = "redis_client"
MIN_LENGTH = 4
FORMATTER = "shorten"
COUNTER_KEY = "{formatter}:counter_key".format(formatter=FORMATTER)