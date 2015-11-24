import os
from flask import render_template

from .. import dovesoft
from ..dovesoft.exceptions import DoveSoftClientError
from notifications import Notification
from .. import app
from ..config import smsconf
from ..config.subscriber_config import get_template_name

ds = dovesoft.DoveSoftClient(smsconf.USERNAME, smsconf.KEY)


class Sms(Notification):

    def __init__(self, **kwargs):
        super(Sms, self).__init__(**kwargs)

    def get_templates(self, template_name, **kwargs):
        """
        Get text templates for sms
        """
        text = render_template("%s.txt" % template_name, **kwargs)
        return text

    def get_message(self, **kwargs):
        """
        Get message object for sms
        """
        message = dovesoft.Sms()

        for key in kwargs.keys():
            if key not in kwargs.get("ignore", smsconf.IGNORE_KEYS):
                fun = getattr(message, "set_{key}".format(key=key))
                fun(kwargs.get(key, ""))

        return message

    def send_message(self, message):
        """
        Send message to receiver via gateway
        """
        try:
            msg = ds.send(message)
            app.logger.info("Successfully sent message: {msg}".format(msg=msg))
            return msg
        except DoveSoftClientError as sgce:
            app.logger.error("Error while sending email: {msg}".format(msg=msg))
            app.logger.error("Email: {message}".format(message=message))
            raise DoveSoftClientError(sgce.code, sgce.read())

    def message_notifier(self, **kwargs):
        """
        Message notifier helper to send message
        """
        template_name = os.path.join(kwargs.get("msg_type", ""), kwargs.get("author", ""),
                                     get_template_name(kwargs.get("category", "")))
        kwargs = self.del_keys(kwargs.get("delete", smsconf.DELETE_KEYS), **kwargs)
        text = self.get_templates(template_name=template_name, **kwargs)
        message = self.get_message(message=text, **kwargs)
        resp = self.send_message(message)
        app.logger.info("{error} with {res}".format(error=resp[0], res=str(resp[1]).strip("\r\n").rstrip("\n\n")))