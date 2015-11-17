__author__ = 'leena'


from libapp import celeryd

from publisher import publish_msg, subscribe_msg


@celeryd.task(priority=0)
def transform_data(source_q, dest_q):
    publish_msg(source_q, dest_q)


@celeryd.task(priority=1)
def subscribe_data():
    subscribe_msg()

