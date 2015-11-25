
import ast
import json
import redis
from .notifications.email import Email
from .notifications.sms import Sms
from .config import libconf, smsconf
from . import app, pubsubd


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
            to = mail_dict.get("to", "")
            category = mail_dict.get("category", "")
            author = mail_dict.get("author", "")
            message_content = mail_dict.get("message_content", "")
            if isinstance(message_content, unicode):
                app.logger.info("Data: {data}".format(data=message_content))
                message_content = ast.literal_eval(message_content)

            if msg_type == "email":
                # It is email
                from_email = mail_dict.get("from_email", "")
                subject = mail_dict.get("subject", "")

                # Call email notifier
                email_obj = Email()
                email_obj.message_notifier(msg_type=msg_type, from_email=from_email, to=to, category=category,
                                           author=author, subject=subject, message_content=message_content)
            elif msg_type == "sms":
                # It is sms
                senderid = mail_dict.get("senderid", smsconf.SENDERID.OFFICE.name)
                accusage = mail_dict.get("accusage", smsconf.ACCUSAGE.trans.value)

                # Call sms notifier
                sms_obj = Sms()
                sms_obj.message_notifier(msg_type=msg_type, senderid=senderid, mobile=to,category=category, author=author,
                                         accusage=accusage, message_content=message_content)
            elif msg_type == "push":
                # It is Push notification
                pass
            else:
                # Its a web notification
                pass