__author__ = 'leena'

import redis
import json
import ast

from libapp import app
from libapp import pubsubd
from libapp.config import libconf, smsconf
from emails import message_notifier
from smss import message_notifier as sms_notifier

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
            msg_type = mail_dict.get("msg_type", "")
            category = mail_dict.get("category", "")
            author = mail_dict.get("author", "")
            from_email = mail_dict.get("from_email", "")
            subject = mail_dict.get("subject", "")
            recipient = mail_dict.get("recipient", "")
            message_content = mail_dict.get("message_content", "")
            if isinstance(message_content, unicode):
                app.logger.info("Data: {data}".format(data=message_content))
                message_content = ast.literal_eval(message_content)

            # Call email notifier
            message_notifier(msg_type=msg_type, category=category, author=author, from_email=from_email, recipient=recipient,
                             subject=subject, message_content=message_content)


def send_sms():
    sms_notifier(mobile=9821804409, senderid=smsconf.SENDERID.OFFICE.name, accusage=smsconf.ACCUSAGE.trans.value,
                 category="enq_created", author="seeker", type="sms")