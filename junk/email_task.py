__author__ = 'leena'

from libapp.emails import email_notifier
from celerytest import celery
from libapp.config import libconf


@celery.task
def send_email():
    email_content = {'name':"LEENA"}
    email_notifier("space_progress", "provider", libconf.SENDER, libconf.RECIPIENT, "Test", email_content=email_content)
