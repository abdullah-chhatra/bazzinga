import os


HOST = "localhost"
PORT = 9001
DEBUG = True
THREADED = True

# flask template and static file configurations
TEMPLATE_DIR = os.path.join(os.getcwd(), "libapp", "templates")
STATIC_PATH = os.path.join(os.getcwd(), "libapp", "static")

# Log configurations
LOG_FILE_NAME = "{log}.log"
LOG_FILE_PATH = os.path.join("logs")
LOG_ROTATION_WHEN = "midnight"
LOG_BACKUP_COUNT = 7
LOG_UTC_STATUS = True
LOG_FORMATTER = "%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s"

# Redis configurations
REDIS_HOST = "localhost"
REDIS_PORT = 6379
# DB List
DB_INDEX = 0

# Send grid configuration
SG_USER = "hello@mycuteoffice.com"
SG_PASS = "mycuteofficeemail"

# Publisher Queue list
PUB_EMAIL_Q = "email-pub"
PUB_SMS_Q = "sms-pub"
PUB_PUSH_Q = "push-pub"
# Celery Queue list
EMAIL_Q = "email"
SMS_Q = "sms"
PUSH_Q = "push"

# Email config
SENDER = "hello@mycuteoffice.com"
RECIPIENT = ["leenakhote23@gmail.com", "khoteleena5@gmail.com", "srahul07@gmail.com"]
