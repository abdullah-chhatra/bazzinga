__author__ = 'leena'

from celery import Celery

@celery.task
def my_background_task(arg1, arg2):
    result = arg1 + arg2
    return result
