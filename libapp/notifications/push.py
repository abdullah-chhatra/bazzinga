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
        Get message object for push
        """
        message = {}
        message['data'] = {}

        for key in kwargs.keys():
            if key not in kwargs.get("ignore", pushconf.IGNORE_KEYS):
                if key == "registration_id" and kwargs.get(key, None) is not None:
                    message[key] = kwargs.get(key, "")
                elif key == "registration_ids" and kwargs.get(key, None) is not None:
                    message[key] = kwargs.get(key, "")
                elif key == "topic" and kwargs.get("topic", None) is not None:
                    message[key] = kwargs.get(key, "")
                elif kwargs.get(key, None) is not None:
                    message['data'].update({key: kwargs.get(key, "")})
                else:
                    # Not sure what to do ;)
                    pass

        return message

    def send_message(self, message):
        """
        Send message to receiver via gateway
        """
        if "registration_id" in message:
            resp = gs.plaintext_request(**message)
        elif "registration_ids" in message:
            resp = gs.send_downstream_message(**message)
        else:
            resp = gs.send_topic_message(**message)
        return resp

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
            app.logger.info("response with {error}".format(error=resp))
        else:
            app.logger.error("No template data available: {data}".format(data=kwargs.keys()))