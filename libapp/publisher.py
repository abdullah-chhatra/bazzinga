__author__ = 'leena'

import redis
import json
import ast

from libapp import app
from libapp import pubsubd
from config import libconf, smsconf
from emails import message_notifier
from sms import message_notifier as sms_notifier


queue = redis.StrictRedis(host=libconf.REDIS_HOST, port=libconf.REDIS_PORT, db=libconf.DB_INDEX)


def publish_msg(source_q=libconf.PUB_EMAIL_Q, dest_q=libconf.EMAIL_Q):
    q_length = queue.llen(source_q)
    app.logger.info("Publisher {queue} length: {data}".format(queue=source_q, data=q_length))
    if q_length > 0:
        for x in range(q_length):
            mail_data = queue.rpop(source_q)
            queue.publish(dest_q, mail_data)


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
            message_notifier("email", category, author, sender, recipient, subject, email_content=email_content)


def send_sms():
    sms_notifier(mobile=9821804409, senderid=smsconf.SENDERID.OFFICE.name, accusage=smsconf.ACCUSAGE.trans.value,
                 category="enq_created", author="seeker", type="sms")