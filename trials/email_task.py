__author__ = 'leena'

from emails import email_notifier
from celerytest import celery
from config.library import SENDER, RECIPIENT

@celery.task
def send_email():
    email_content = {'name':"LEENA"}
    email_notifier("space_progress", "provider", SENDER, RECIPIENT, "Test", email_content=email_content)
