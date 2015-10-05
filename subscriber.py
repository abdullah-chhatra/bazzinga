__author__ = 'leena'

import redis
import time
import json
from flask import Flask
from emails import email_notifier
from flask import render_template
from config import library as settings


r = redis.StrictRedis(host=settings.HOST, port=settings.PORT, db=settings.DB_INDEX)
p = r.pubsub()
p.subscribe(settings.EMAIL_Q)


app = Flask(__name__, template_folder=settings.TEMPLATE_DIR)


def subscribe_data():
    while True:
        message = p.get_message()
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


@app.route("/")
def index():
    subscribe_data()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)