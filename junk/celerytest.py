__author__ = 'leena'

from celery import Celery

celeryObj = Celery(include=['email_task'])

celeryObj.config_from_object('libapp.config.libconf')


if __name__ == "__main__":
    celeryObj.start()