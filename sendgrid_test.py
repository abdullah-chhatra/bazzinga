__author__ = 'zeba'

import sendgrid
from sendgrid import SendGridClient, Mail

sg = sendgrid.SendGridClient('hello@mycuteoffice.com', 'mycuteofficeemail')

message = sendgrid.Mail()
message.add_to('zeba dhongre <zebadhongre8@gmail.com>')
message.set_subject('Example')
message.set_html('Body')
message.set_text('Body')
message.set_from('leena khote<leenakhote23@gmail.com>')
status, msg = sg.send(message)