__author__ = 'leena'

#from libapp.emails import email_notifier
#from libapp import celeryd
from libapp.tasks import subscribe_data
#from libapp.config import libconf


#@celeryd.task()
def send_email():
    subscribe_data()