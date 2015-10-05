__author__ = 'leena'

import os

from flask import render_template

import sendgrid
from sendgrid.exceptions import (SendGridClientError)
from config.subscriber_config import get_template_name
from config import library as settings


sg = sendgrid.SendGridClient(settings.SG_USER, settings.SG_PASS)


def generate_template(template_name, **kwargs):
    html = render_template("%s.html" % template_name, **kwargs)
    text = render_template("%s.txt" % template_name, **kwargs)
    return html, text


def generate_message(recipients, subject, html_body, text_body, sender, category):
    message = sendgrid.Mail()
    message.add_to(recipients)
    message.set_subject(subject)
    message.set_html(html_body)
    message.set_text(text_body)
    message.set_from(sender)
    message.add_category(category)
    return message


def send_email(message):
    try:
        msg = sg.send(message)
        return msg
    except SendGridClientError as sgce:
        raise SendGridClientError(sgce.code, sgce.read())


def email_notifier(category, author, sender, recipient, subject, **kwargs):
    template_name = os.path.join(author, get_template_name(category))
    html, text = generate_template(template_name=template_name, **kwargs)
    message = generate_message(recipients=recipient, subject=subject,
                               html_body=html, text_body=text,
                               sender=sender, category=category)
    send_email(message)