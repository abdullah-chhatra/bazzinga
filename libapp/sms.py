
import os
import dovesoft
from dovesoft.exceptions import DoveSoftClientError
from flask import render_template
from config.subscriber_config import get_template_name
from libapp import app
import config.smsconf as settings


ds = dovesoft.DoveSoftClient(settings.USERNAME, settings.KEY)


def generate_template(template_name, **kwargs):
    text = render_template("%s.txt" % template_name, **kwargs)
    return text


def generate_message(**kwrgs):
    message = dovesoft.Sms()

    for key in kwrgs.keys():
        fun = getattr(message, "set_{key}".format(key=key))
        fun(kwrgs.get(key, ""))

    return message


def send_message(message):
    try:
        msg = ds.send(message)
        app.logger.info("Successfully sent message: {msg}".format(msg=msg))
        return msg
    except DoveSoftClientError as sgce:
        app.logger.error("Error while sending email: {msg}".format(msg=msg))
        app.logger.error("Email: {message}".format(message=message))
        raise DoveSoftClientError(sgce.code, sgce.read())


def message_notifier(**kwargs):
    template_name = os.path.join(kwargs.get("type", ""), kwargs.get("author", ""), get_template_name(kwargs.get("category", "")))
    kwargs = del_keys(["type", "author", "category"], **kwargs)
    text = generate_template(template_name=template_name, **kwargs)
    message = generate_message(message=text, **kwargs)
    send_message(message)


def del_keys(keys, **kwargs):
    for key in keys:
        del kwargs[key]
    return kwargs
