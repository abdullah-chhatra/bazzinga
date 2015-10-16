__author__ = 'leena'

from emails import email_notifier
from libapp import celeryd
from libapp.subscriber import subscribe_data
from config import libconf


@celeryd.task()
def send_email():
    #email_content = {'name':"LEENA"}
    #email_notifier("space_progress", "provider", libconf.SENDER, libconf.RECIPIENT, "Test", email_content=email_content)
    subscribe_data()