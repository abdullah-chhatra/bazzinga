__author__ = 'leena'

import redis
import time
import pickle
import json
import os
from flask import Flask
from emails import email_notifier
from flask import render_template

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('lee')

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

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