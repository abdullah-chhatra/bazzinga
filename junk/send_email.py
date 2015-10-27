__author__ = 'leena'

from flask import Flask
from flask_mail import Mail, Message
import sendgrid
from sendgrid import SendGridClient, Mail
from sendgrid.exceptions import (SendGridClientError)
from flask import render_template


app =Flask(__name__)

app.config.update(
   DEBUG=True,
   #EMAIL SETTINGS
   MAIL_SERVER='smtp.gmail.com',
   MAIL_PORT=465,
   MAIL_USE_SSL=True,
   MAIL_USERNAME = 'hello@mycuteoffice.com',
   MAIL_PASSWORD = 'mycuteofficeemail'
   )
print "Let's talk about flask"

@app.route("/")
def index():
    try :
        sg = sendgrid.SendGridClient('hello@mycuteoffice.com', 'mycuteofficeemail')

        message = sendgrid.Mail()
        message.add_to('leena khote<leenakhote23@gmail.com>')
        message.set_subject('Example')
        message.set_html('Body')
        message.set_text('Body')
        message.set_from('zeba dhongre<zebaddhongre8@gmail.com>')
        status, msg = sg.send(message)
    except SendGridClientError as sgce:
        raise SendGridClientError(sgce.code , sgce.read())
    return "heelo zebu"

if __name__ == "__main__":
    app.run()
