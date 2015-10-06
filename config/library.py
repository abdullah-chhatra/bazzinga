import os


HOST = "localhost"
PORT = 6379

TEMPLATE_DIR = os.path.join(os.getcwd(), "templates")  #os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

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
RECIPIENT = ["dhongre.zeba@gmail.com", "khoteleena5@gmail.com"]