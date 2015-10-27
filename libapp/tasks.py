__author__ = 'leena'


from libapp import celeryd

from publisher import publish_msg, subscribe_msg


@celeryd.task(priority=0)
def transform_data():
    publish_msg()


@celeryd.task(priority=1)
def subscribe_data():
    subscribe_msg()

