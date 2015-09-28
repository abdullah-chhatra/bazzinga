__author__ = 'leena'

import os
from flask import Flask
from flask import render_template
import jinja2
from flask_mail import Mail, Message
import sendgrid
from sendgrid import SendGridClient, Mail
from sendgrid.exceptions import (SendGridClientError)
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sg = sendgrid.SendGridClient('hello@mycuteoffice.com', 'mycuteofficeemail')


def get_email_template(template_name, name):
    html = render_template("%s.html" % template_name, name=name)
    text = render_template("%s.txt" % template_name, name=name)
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


def generate_email(category, template_name, sender, recipient, subject, name):
    html, text = get_email_template(template_name=template_name, name=name)
    message = generate_message(recipients=recipient, subject=subject,
                               html_body=html, text_body=text,
                               sender=sender, category=category)
    send_email(message)

def get_subject(category):
    return {
            "space_progress"  : "space completion progress",
            "space_status_change" : "space_status_change",
            "space_status_complete" :"space_status_complete",
            "enquiry_space" : "enquiry addded to space",
            "enquiry_reply" : "rwply to enquiry",
            "enquiry_status" : "enquiry status",
            "enquiry_closed" : "enquiry closed",
            "enquiry_accept_reject" : "enquiry accept / reject",
            "enquiry_created" : "enquiry created",
            "book_new" : "new booking",
            "book_status" : "booking status ",
            "book_reminder" : "booking reminder",
            "book_cancel" : "booking cancel",
            "book_cancel_confirm" : "book cancel/confirm",
            "book_incomp_reminder": "booking incomplete reminder",
            "book_receipt" : "booking receipt",
            "requirement_created" : "requirement created",
            "requirement_reminder" : "requirement reminder",
            "requirement_suggestion" : "requirement suggestion",
            "requirement_new" : "requirement new",
            "requirement_reply" : "requirement rely",
            "requirement_noreply" : "requirement noreply",
            "revoke_space" : "revoke space",
            "space_awaited_approval" : "space awaited / approval",
            "feedback_space" : "space feedback",
            "feedback_system" : "system feedback",
            "change_password" : "change password"

    }[category]

def get_template_(category,author):
    return {"space_progress"  : author+"/space_progress_email",
            "space_status_change" : author+"/space_status_change",
            "space_status_complete" : author+"/space_status_complete",
            "enquiry_space" : author+"/enq_space",
            "enquiry_reply" : author+"/enq_reply",
            "enquiry_status" : author+"/enq_status",
            "enquiry_closed" : author+"/enq_closed",
            "enquiry_accept_reject" : author+"enq_accpt_rej",
            "enquiry_created" : author+"enq_created",
            "book_new" : author+"/book_new",
            "book_status" : author+"/book_status",
            "book_reminder" : author+"/book_reminder",
            "book_cancel" : author+"/book_cancel",
            "book_cancel_confirm" : author+"/book_cancel_confirm",
            "book_incomp_reminder": author +"/book_incomp_rem",
            "book_receipt" : author +"/book_receipt",
            "requirement_created" : author +"/req_created",
            "requirement_reminder" : author +"/req_reminder",
            "requirement_suggestion" :author + "/req_suggestion",
            "requirement_new" : author + "/req_new",
            "requirement_reply" : author + "/req_reply",
            "requirement_noreply" : author + "/req_noreply",
            "revoke_space" : author + "/revoke_space",
            "space_awaited_approval" : author + "/space_await_approval",
            "feedback_space" : author+"/feedback_space",
            "feedback_system" : author+"/feedback_system",
            "change_password" : author + "/changepassword"

    }[category]

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

@app.route("/")
def hello():
    name= "leena"
    author = "space_provider"
    category = "feedback_system"
    subject = get_subject(category)
    template_name = get_template_(category,author)
    recipient = ["khote.leena5@gmail.com"]
    generate_email(category=category, template_name=template_name, subject=subject, name="Zeba", recipient=recipient, sender="hello@mycuteoffice.com")
    return render_template("index.html", name= name)


if __name__ == "__main__":
    app.run(debug=True)
