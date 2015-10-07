__author__ = 'leena'


from celery import Celery
#from config import celerytest as settings
from emails import email_notifier

celery = Celery(include=['trials.email_task'])

celery.config_from_object('config.library')


if __name__ == "__main__":
    celery.start()