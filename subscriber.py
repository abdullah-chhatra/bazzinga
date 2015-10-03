__author__ = 'leena'

import redis
import time
import pickle
import json
import os
from flask import Flask
from emails import email_data
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
            if type(data) is not long and data:
                category = json.loads(data)['category']
                author = json.loads(data)['author']
                sender = json.loads(data)['sender']
                subject = json.loads(data)['subject']
                receiver = json.loads(data)['receiver']
                print category , author, sender , receiver , subject
                email_data(category , author , sender , receiver , subject)
            time.sleep(0.5)

@app.route("/")
def index():
    subscribe_data()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)