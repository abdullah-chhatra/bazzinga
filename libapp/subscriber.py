__author__ = 'leena'


import json
import redis

from libapp import app
from libapp import pubsubd
from libapp import celeryd
from emails import email_notifier
from config import libconf


@celeryd.task()
def publish_msg():
    queue = redis.StrictRedis(host=libconf.REDIS_HOST, port=libconf.REDIS_PORT, db=libconf.DB_INDEX)
    q_length = queue.llen(libconf.EMAIL_Q + '-pub')
    for x in range(q_length):
        mail_data = queue.lpop(libconf.EMAIL_Q + '-pub')
        queue.publish(libconf.EMAIL_Q, mail_data)
    # d = json.loads(data)
    # sender = d.get("sender", settings.SENDER)
    # recipient = d.get("recipient", settings.RECIPIENT)
    # msg = get_msg(sender, recipient)
    # queue.publish(libconf.EMAIL_Q, data)


@celeryd.task()
def subscribe_data():
    message = pubsubd.get_message()
    if message:
        data = message.get('data')
        app.logger.info("Subscriber read: {data}".format(data=data))
        if data and type(data) is not long:
            mail_dict = json.loads(data)
            category = mail_dict.get("category", "")
            author = mail_dict.get("author", "")
            sender = mail_dict.get("sender", "")
            subject = mail_dict.get("subject", "")
            recipient = mail_dict.get("recipient", "")
            email_content = mail_dict.get("email_content", "")

            # Call email notifier
            email_notifier(category, author, sender, recipient, subject, email_content=email_content)

