__author__ = 'zeba'

import os
from flask import Flask
from flask_mail import Mail, Message
import sendgrid
from sendgrid import SendGridClient, Mail
from sendgrid.exceptions import (SendGridClientError)
from flask import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sg = sendgrid.SendGridClient('hello@mycuteoffice.com', 'mycuteofficeemail')

def generate_message(recipients,subject,html_body,text_body,sender):
    message = sendgrid.Mail()
    message.add_to(recipients)
    message.set_subject(subject)
    message.set_html(html_body)
    message.set_text(text_body)
    message.set_from(sender)
    return message

def send_email(message):
    try :
        msg = sg.send(message)
    except SendGridClientError as sgce :
        raise SendGridClientError(sgce.code , sgce.read())

def get_email_template(template_name):
    html = render_template("%s.html" % template_name)
    text = render_template("%s.txt" % template_name)
    return html, text

def send_changepassword_email(recipient='zeba dhongre<zeba@mailinator.com>'):
    html, text = get_email_template("space_provider/systemfeedback")
    message = generate_message( [recipient], "Feedback Please!!!" ,html, text,
                               'zeba dhongre<zebadhongre8@gmail.com>')
    send_email(message)


app = Flask(__name__, template_folder= os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

@app.route("/")
def hello():
    send_changepassword_email('zeba dhongre<zeba@mailinator.com>')
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)