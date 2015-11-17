__author__ = 'leena'

import redis
import json
import ast

from libapp import app
from libapp import pubsubd
from config import libconf
from emails import message_notifier


queue = redis.StrictRedis(host=libconf.REDIS_HOST, port=libconf.REDIS_PORT, db=libconf.DB_INDEX)


def publish_msg():
    q_length = queue.llen(libconf.PUB_EMAIL_Q)
    app.logger.info("Publisher q length: {data}".format(data=q_length))
    if q_length > 0:
        for x in range(q_length):
            mail_data = queue.rpop(libconf.PUB_EMAIL_Q)
            queue.publish(libconf.EMAIL_Q, mail_data)


def subscribe_msg():
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
            if isinstance(email_content, unicode):
                app.logger.warning("Data: {data}".format(data=email_content))
                email_content = ast.literal_eval(email_content)

            # Call email notifier
            message_notifier(category, author, sender, recipient, subject, email_content=email_content)

