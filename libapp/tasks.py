__author__ = 'leena'


from libapp import celeryd
from libapp import app
#from publisher import publish_msg, subscribe_msg
from sender import publish_msg, subscribe_msg

@celeryd.task(priority=0)
def transform_data(source_q, dest_q):
    publish_msg(source_q, dest_q)
    """
    source_queues = [libconf.PUB_EMAIL_Q, libconf.PUB_SMS_Q, libconf.PUSH_Q]
    dest_queues = [libconf.EMAIL_Q, libconf.SMS_Q, libconf.PUSH_Q]
    for source_q, dest_q in zip(source_queues, dest_queues):
        app.logger.error("{source} > {dest}".format(source=source_q, dest=dest_q))
        publish_msg(source_q, dest_q)
    """


@celeryd.task(priority=1)
def subscribe_data():
    subscribe_msg()

