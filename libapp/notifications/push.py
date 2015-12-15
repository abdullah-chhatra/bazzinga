import os
import gcm
from flask import render_template
from .notifications import Notification
from .. import app
from ..config import pushconf

gs = gcm.GCM(pushconf.API_KEY, debug=pushconf.DEBUG)


class Push(Notification):

    def __init__(self, **kwargs):
        super(Push, self).__init__(**kwargs)

    def get_templates(self, template_name, **kwargs):
        """
        Get text templates for push
        """
        text = render_template("{template}.txt".format(template=template_name), **kwargs)
        return text

    def get_message(self, **kwargs):
        """
        Get message object for email
        """
        message = {}

        for key in kwargs.keys():
            if key not in kwargs.get("ignore", pushconf.IGNORE_KEYS):
                func = None
                if key not in ["to", "to_name", "cc", "bcc", "content_id", "category"]:
                    if key not in ["from_email", "reply_to"]:
                        func = getattr(message, "set_{key}".format(key=key))
                    elif key == "reply_to":
                        func = getattr(message, "set_replyto")
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
        gcm.send()
        pass

    def message_notifier(self, **kwargs):
        """
        Message notifier helper to send message
        """
        if all(key in kwargs for key in ["msg_type", "author", "category"]):
            template_name = os.path.join(kwargs.get("msg_type", ""), kwargs.get("author", ""),
                                         kwargs.get("category", ""), kwargs.get("template", ""))
            kwargs = self.del_keys(kwargs.get("delete", pushconf.DELETE_KEYS), **kwargs)
            text = self.get_templates(template_name=template_name, **kwargs)
            message = self.get_message(text=text, **kwargs)
            resp = self.send_message(message)
            app.logger.info("{error} with {response}".format(error=resp[0], response=resp[1]))
        else:
            app.logger.error("No template data available: {data}".format(data=kwargs.keys()))