__author__ = 'rahul'

from celery import Celery
from ..config import celconf


def init_app(app):
    # configure app for celery
    app.config['CELERY_TIMEZONE'] = celconf.CELERY_TIMEZONE
    app.config["CELERY_ACCEPT_CONTENT"] = celconf.CELERY_ACCEPT_CONTENT
    app.config["CELERY_PREFETCH_MULTIPLIER"] = celconf.CELERY_PREFETCH_MULTIPLIER
    app.config["CELERY_ACKS_LATE"] = celconf.CELERY_ACKS_LATE
    app.config["BROKER_TRANSPORT"] = celconf.BROKER_TRANSPORT
    app.config["CELERY_BROKER_URL"] = celconf.BROKER_URL
    app.config["CELERY_RESULT_BACKEND"] = celconf.CELERY_RESULT_BACKEND

    celeryd = Celery(app.import_name, broker=celconf.BROKER_URL)
    celeryd.conf.update(app.config)

    TaskBase = celeryd.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celeryd.Task = ContextTask

    return celeryd
