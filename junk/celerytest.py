__author__ = 'leena'

from celery import Celery

celery = Celery(include=['junk.email_task'])

celery.config_from_object('config.library')


if __name__ == "__main__":
    celery.start()