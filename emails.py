__author__ = 'leena'

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

def get_email_template(template_name):
    html = render_template("%s.html" % template_name)
    text = render_template("%s.txt" % template_name)
    return html, text

def generate_message(recipients,subject,html_body,text_body,sender ,category):
    message = sendgrid.Mail()
    message.add_to(recipients)
    message.set_subject(subject)
    message.set_html(html_body)
    message.set_text(text_body)
    message.set_from(sender)
    message.add_category(category)
    return message

def send_email(message):
    try :
        msg = sg.send(message)
    except SendGridClientError as sgce :
        raise SendGridClientError(sgce.code , sgce.read())

def generate_email(category, template_name, sender, recipient, subject):
    html,text = get_email_template(template_name=template_name)
    message = generate_message(recipients=recipient, subject=subject, html_body=html, text_body=text,
                               sender=sender, category=category)
    send_email(message)

def get_template_details(category):
    subject = None
    template_name = None
    if category == "change password" :
        subject = "your password has been changed"
        template_name = "changepassword"
    elif category == "space_provider_space_progress":
        subject = "space completion progress"
        template_name = "space_provider/space_progress_email"
    elif category == "space_provider_space_status_changed":
        subject = "space status is changed"
        template_name = "space/provider/space_status_change"
    elif category == "space_provider_space_status_complete" :
        subject = "space status is complete"
        template_name = "space_provider/space_status_complete"
    elif category == "space_provider_enquiry_space":
        subject = "enquiry added to space"
        template_name = "space_provider/enq_space"
    elif category == "space_provider_enquiry_reply":
        subject = "rply posted to enquiry"
        template_name = "space_provider/enq_rply"
    elif category == "space_provider_enquiry_status":
        subject = "enquiry status changed"
        template_name = "space_provider/enq_status"
    elif category == "space_provider_new_booking":
        subject = "New Booking intimation"
        template_name ="space_provider/new_booking_intimation"
    elif category == "space_provider_booking_status":
        subject = "booking status changed"
        template_name ="space_provider/booking_status_change"
    elif category == "space_provider_booking_reminder":
        subject = "Reminder of visit"
        template_name = "space_provider/booking_reminder"
    elif category == "space_provider_booking_cancel":
        subject = "Seekers request to cancel booking"
        template_name = "space_provider/booking_cancel_req"
    elif category == "space_provider_booking_cancel_confirm":
        subject = "Admins confirmation to cancel booking"
        template_name = "space_provider/booking_cancel_confirm"
    elif category == "space_provider_feedback_space":
        subject = "Feedback about Space seeker"
        template_name = "space_provider/space_seeker_feedback"
    elif category == "space_provider_feedback_system":
        subject = "Feedback about system"
        template_name = "space_provider/systemfeedback"
    elif category == "space_seeker_enquiry_created":
        subject = "enquiry created"
        template_name = "space_provider/space_seeker/ss_enq_created"
    elif category == "space_seeker_enquiry_reply":
        subject = "Reply to enquiry by space owner or admin"
        template_name = "space_seeker/ss_enq_reply"
    elif category == "space_seeker_enquiry_status":
        subject = "Enquiry status"
        template_name = "space_seeker/ss_enq_accpt_rej"
    elif category == "space_seeker_enquiry_closed":
        subject = "Enquiry closed by automated process for inactivity"
        template_name = "space_seeker/ss_enq_closed"
    elif category == "space_seeker_requirement_created":
        subject = "New requirement created"
        template_name = "space_seeker/ss_req_created"
    elif category == "space_seeker_requirement_suggestion":
        subject = "Suggestions based on requirement"
        template_name = "space_seeker/ss_req_suggestion"
    elif category == "space_seeker_requirement_reminder":
        subject = "Reminder for more suggestions"
        template_name = "space_seeker/ss_req_reminder"
    elif category == "space_seeker_booking_incomplete":
        subject = "Booking incmplete reminder"
        template_name = "space_seeker/ss_book_incomp_rem"
    elif category == "space_seeker_booking_receipt":
        subject = "Booking receipt"
        template_name = "space_seeker/ss_book_receipt"
    elif category == "space_seeker_booking_status":
        subject = "Booking status"
        template_name = "space_seeker/ss_book_status"
    elif category == "space_seeker_booking_reminder":
        subject = "Reminder to visit"
        template_name = "space_seeker/ss_book_reminder"
    elif category == "space_seeker_booking_cancel":
        subject = "Request to cancel booking"
        template_name = "space_seeker/ss_book_cancel"
    elif category == "space_seeker_booking_cancel_confirm":
        subject = "Cancel booking approval or disapproval by admin"
        template_name = "space_seeker/ss_book_cancel_confirm"
    elif category == "space_seeker_feedback_space":
        subject = "Feedback about Space owner"
        template_name = "space_seeker/ss_feedback_spaceowner"
    elif category == "space_seeker_feedback_system":
        subject = "Feedback about system"
        template_name = "space_seeker/ss_feedback_system"
    elif category == "admin_space_approval_waiting":
        subject = "Space waiting for approval"
        template_name = "admin/admin_space_await_approval"
    elif category == "admin_space_revoked":
        subject = "Revoked space"
        template_name = "admin/admin_revoke_space"
    elif category == "admin_new_city_added":
        subject = "New city addition"
        template_name = "admin/admin_new_cityadd"
    elif category == "admin_enquiry_created":
        subject = "New enquiry created"
        template_name = "admin/admin_enq_created"
    elif category == "admin_enquiry_reply":
        subject = "Reply to enquiry by space owner or space seeker"
        template_name = "admin/admin_enq_reply"
    elif category == "admin_enquiry_status":
        subject = "Enquiry accept / reject by space owner"
        template_name = "admin/admin_enq_status"
    elif category == "admin_requirement_owner_noreply":
        subject = "No reply by owner for 48 hours"
        template_name = "admin/admin_req_owner_noreply"
    elif category == "admin_requirement_created":
        subject = "new requirement"
        template_name = "admin_req_new"
    elif category == "admin_requirement_reply":
        subject = "Reply by space seeker to reminder for more suggestion"
        template_name = "admin/admin_req_reply"
    elif category == "admin_booking_created":
        subject = "New booking"
        template_name = "admin/admin_booking_new"
    elif category == "admin_booking_owner_noreply":
        subject = "No reply by owner for approval for more than 12 hours"
        template_name = "admin_booking_noreply12hr"
    elif category == "admin_booking_status":
        subject = "Accept / reject booking by owner"
        template_name = "admin_booking_status"
    elif category == "admin_booking_cancel":
        subject = "Request to cancel booking by seeker"
        template_name = "admin_cancel_booking"

    return subject, template_name

app = Flask(__name__, template_folder= os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

@app.route("/")
def hello():
    category = "change password"
    recipient = ["zebadhongre8@gmail.com"]
    subject, template_name = get_template_details(category=category)
    generate_email(category=category, template_name=template_name, subject=subject, recipient=recipient, sender="hello@mycuteoffice.com")
    #generate_email('leena khote<leenakhote23@gmail.com>')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)