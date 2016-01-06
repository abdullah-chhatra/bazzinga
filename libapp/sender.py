
import ast
import json
import redis
from .notifications.email import Email
from .notifications.sms import Sms
from .notifications.push import Push
from .config import libconf, smsconf, pushconf
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
    while message is not None:
        data = message.get('data')
        app.logger.info("Subscriber read: {data}".format(data=data))
        if data and type(data) is not long:
            msg_dict = json.loads(data)
            msg_type = msg_dict.get("msg_type", "")
            to = msg_dict.get("to", "")
            category = msg_dict.get("category", "")
            author = msg_dict.get("author", "")
            template = msg_dict.get("template", "")
            message_content = msg_dict.get("message_content", "")

            if isinstance(message_content, unicode):
                app.logger.info("Error: {data}".format(data=type(message_content)))
                app.logger.info("Data: {data}".format(data=message_content))
                message_content = ast.literal_eval(message_content)

            if msg_type == "email":
                # It is email notification
                from_email = msg_dict.get("from_email", "")
                subject = msg_dict.get("subject", "")

                # Call email notifier
                email_obj = Email()
                email_obj.message_notifier(msg_type=msg_type, author=author, category=category, template=template,
                                           from_email=from_email, to=to, subject=subject,
                                           message_content=message_content)
            elif msg_type == "sms":
                # It is sms notification
                senderid = msg_dict.get("senderid", smsconf.SENDERID.OFFICE.name)
                accusage = msg_dict.get("accusage", smsconf.ACCUSAGE.trans.value)

                # Call sms notifier
                sms_obj = Sms()
                sms_obj.message_notifier(msg_type=msg_type, author=author, category=category, template=template,
                                         senderid=senderid, mobile=to, accusage=accusage,
                                         message_content=message_content)
            elif msg_type == "push":
                # It is Push notification
                is_json = msg_dict.get("is_json", False)
                retries = msg_dict.get("retries", pushconf.RETRIES)

                registration_id = None
                registration_ids = None
                if to and len(to) == 1:
                    registration_id = to[0]
                    is_json = False
                elif to and len(to) > 1:
                    registration_ids = to
                else:
                    pass
                """
                registration_id = msg_dict.get("registration_id", None)
                if "registration_ids" in msg_dict and len(msg_dict.get("registration_ids")) == 1:
                    registration_id = msg_dict.get("registration_ids")[0]
                    del msg_dict["registration_ids"]
                    is_json = False

                registration_ids = msg_dict.get("registration_ids", None)
                """
                # Call push notifier
                push_obj = Push()
                push_obj.message_notifier(msg_type=msg_type, author=author, category=category, template=template,
                                          is_json=is_json, retries=retries, registration_ids=registration_ids,
                                          registration_id=registration_id, message_content=message_content)
            else:
                # Its a web notification
                pass

        message = pubsubd.get_message()