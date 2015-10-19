__author__ = 'zeba'

import sendgrid
from emailer import email_notifier
from flask import render_template
from sendgrid import SendGridClient, Mail
from subsc import get_template_name

from flask import Flask
from celery import Celery
from config.library import SENDER, RECIPIENT

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('celery_flask.html')

@celery.task
def send_async_email():
    email_content = {'name':"LEENA"}
    email_notifier("space_progress", "provider", SENDER, RECIPIENT, "Test", email_content=email_content)