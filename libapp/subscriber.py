__author__ = 'leena'


import json
from libapp import app

from libapp import pubsubd
from emails import email_notifier


def subscribe_data():
    message = pubsubd.get_message()
    if message:
        data = message.get('data')
        app.logger.info("Subscriber read: {data}".format(data=data))
        if data and type(data) is not long:
            mail_dict = json.loads(data)
            category = mail_dict['category']
            author = mail_dict['author']
            sender = mail_dict['sender']
            subject = mail_dict['subject']
            recipient = mail_dict['recipient']
            email_content = mail_dict['email_content']

            # Call email notifier
            email_notifier(category, author, sender, recipient, subject, email_content=email_content)