__author__ = 'leena'


import json
from libapp import app

from libapp import pubsubd
from libapp import celeryd
from emails import email_notifier


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