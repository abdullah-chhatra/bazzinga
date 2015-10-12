import os


HOST = "localhost"
PORT = 9001
DEBUG = True
THREADED = True

TEMPLATE_DIR = os.path.join(os.getcwd(), "libapp", "templates")
STATIC_PATH = os.path.join(os.getcwd(), "libapp", "static")

# Redis configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
# DB List
DB_INDEX = 0

# Send grid configuration
SG_USER = "hello@mycuteoffice.com"
SG_PASS = "mycuteofficeemail"

# Queue list
EMAIL_Q = "email"
SMS_Q = "sms"
PUSH_Q = "push"

# Email config
SENDER = "hello@mycuteoffice.com"
RECIPIENT = ["leenakhote23@gmail.com", "khoteleena5@gmail.com", "srahul07@gmail.com"]
