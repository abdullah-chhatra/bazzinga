__author__ = 'rahul'

from celery import Celery
from ..config import celconf


def init_app(app):
    # configure app for celery
    app.config['CELERY_BROKER_URL'] = celconf.BROKER_URL
    app.config['CELERY_RESULT_BACKEND'] = celconf.CELERY_RESULT_BACKEND
    app.config['BROKER_TRANSPORT'] = celconf.BROKER_TRANSPORT

    celeryd = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celeryd.conf.update(app.config)

    return celeryd
