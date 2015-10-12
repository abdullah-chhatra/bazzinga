__author__ = 'leena'

import time
import json

from libapp import pubsubd
from emails import email_notifier


def subscribe_data():
    while True:
        message = pubsubd.get_message()
        if message:
            data = message.get('data')
            print("Subscriber: %s" % data)
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
            time.sleep(0.5)