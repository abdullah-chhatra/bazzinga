__author__ = 'rahul'


import logging
from logging.handlers import TimedRotatingFileHandler


def init_app(app):
    logfile = "{log}.log".format(log=app.import_name)
    formatter = logging.Formatter("%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s")

    handler = TimedRotatingFileHandler(logfile, when='midnight', backupCount=7, utc=True)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)

    # werkzeug log messages
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

    app.logger.addHandler(handler)
