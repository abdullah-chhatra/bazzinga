import os
from flask import render_template
import sendgrid
from sendgrid.exceptions import SendGridClientError

from notifications import Notification
from .. import app
from ..config import libconf
from ..config.subscriber_config import get_template_name

sg = sendgrid.SendGridClient(libconf.SG_USER, libconf.SG_PASS)


class Email(Notification):

    def __init__(self, **kwargs):
        super(Email, self).__init__(**kwargs)

    def get_templates(self, template_name, **kwargs):
        """
        Get html and text templates for emails
        """
        html = render_template("%s.html" % template_name, **kwargs)
        text = render_template("%s.txt" % template_name, **kwargs)
        return html, text

    def get_message(self, **kwargs):
        """
        Get message object for email
        """
        message = sendgrid.Mail()

        for key in kwargs.keys():
            if key not in ["message_content"]:
                func = None
                if key not in ["to", "to_name", "cc", "bcc", "content_id", "category"]:
                    if key is not "from_email":
                        func = getattr(message, "set_{key}".format(key=key))
                    else:
                        func = getattr(message, "set_from")
                else:
                    func = getattr(message, "add_{key}".format(key=key))
                func(kwargs.get(key, ""))

        return message

    def send_message(self, message):
        """
        Send message to receiver via gateway
        """
        try:
            msg = sg.send(message)
            app.logger.info("Successfully sent message: {msg}".format(msg=msg))
            return msg
        except SendGridClientError as sgce:
            app.logger.error("Error while sending email: {msg}".format(msg=msg))
            app.logger.error("Email: {message}".format(message=message))
            raise SendGridClientError(sgce.code, sgce.read())

    def message_notifier(self, **kwargs):
        """
        Message notifier helper to send message
        """
        template_name = os.path.join(kwargs.get("msg_type", ""), kwargs.get("author", ""), get_template_name(kwargs.get("category", "")))
        kwargs = self.del_keys(["msg_type", "author"], **kwargs)
        html, text = self.get_templates(template_name=template_name, **kwargs)
        message = self.get_message(html=html, text=text, **kwargs)
        self.send_message(message)