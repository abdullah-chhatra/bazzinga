import os


HOST = "localhost"
PORT = 5000

TEMPLATE_DIR = os.path.join(os.getcwd(), "templates")

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
RECIPIENT = ["leenakhote23@gmail.com", "khoteleena5@gmail.com"]