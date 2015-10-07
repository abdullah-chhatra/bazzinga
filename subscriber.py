__author__ = 'leena'

import redis
import time
import json
from flask import Flask
from celery import Celery
from emails import email_notifier
from flask import render_template
from config import library as settings, celerytest as celeryconfig
#from trials.celerytest import celery
from trials.email_task import send_email


r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.DB_INDEX)
p = r.pubsub()
p.subscribe(settings.EMAIL_Q)


app = Flask(__name__, template_folder=settings.TEMPLATE_DIR)

app.config['CELERY_BROKER_URL'] = celeryconfig.BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = celeryconfig.CELERY_RESULT_BACKEND
app.config['BROKER_TRANSPORT'] = celeryconfig.BROKER_TRANSPORT


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


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
    send_email.delay()
    #subscribe_data()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT, debug=True)