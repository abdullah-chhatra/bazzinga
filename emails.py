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


def get_email_template(template_name, **kwargs):
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


def generate_email(category, template_name, sender, recipient, subject, **kwargs):
    html, text = get_email_template(template_name=template_name, **kwargs)
    message = generate_message(recipients=recipient, subject=subject,
                               html_body=html, text_body=text,
                               sender=sender, category=category)
    send_email(message)

def get_subject(category):
    return {
            "space_progress"  : "space completion progress",
            "space_status_change" : "space status change",
            "space_status_complete" :"space_status_complete",
            "space_cityadd" :"New city addition",
            "enquiry_space" : "enquiry addded to space",
            "enquiry_reply" : "rwply to enquiry",
            "enquiry_noreply" : "Enquiry ID: has exceeded 48 hours without a reply",
            "enquiry_status" : "enquiry status",
            "enquiry_closed" : "enquiry closed",
            "enquiry_accept" : "Your enquiry (Enquiry ID: ) has been accepted by the space provider!",
            "enquiry_reject" : "Your enquiry (Enquiry ID: ) has been rejected by the space provider.",
            "enquiry_created" : "Your enquiry for space ID:",
            "book_new" : "new booking",
            "book_accept" : "Status of Booking ID: Accepted",
            "book_reject" : "Status of Booking ID: Rejected",
            "book_reminder" : "Booking reminder (Booking ID:) ",
            "book_cancel" : "Your request to cancel booking ID: ",
            "book_cancel_approve" : "Cancellation for the Booking ID: is Approved",
            "book_cancel_disapp" : "Cancellation for the Booking ID: is Disapproved ",
            "book_incomp_reminder": "Status of Booking ID: - Incomplete",
            "book_receipt" : "Booking Receipt for Booking ID: ",
            "book_invite" : "Invite for meeting",
            "book_meet_cancel" : "Meeting canceled intimation to all attendees",
            "book_noreply" : "Booking confirmation for booking ID: overdue",
            "requirement_created" : ": Your requirement with the ID: is generated.",
            "requirement_reminder" : "Reminder for more suggestions",
            "requirement_suggestion" : "Spaces matching your Requirement ID:",
            "requirement_new" : "requirement new",
            "requirement_reply" : "requirement rely",
            "requirement_noreply" : "requirement noreply",
            "revoke_space" : "Space ID: has been revoked",
            "space_awaited_approval" : " Approval awaiting for Space ID: l",
            "feedback_space" : "Review the Space ID: DEF123",
            "feedback_system" : "Booked a space / conference room through MyCuteOffice.com? Review us.",
            "change_password" : "change password",
            "forgot_password" : "forgot password",
            "invite_referral" : "invitereferral",
            "new_booking" : "new space booking",
            "new_enquiry" : "new space enquiry",
            "new_requirement" : "new space requirement",
            "signup" : "Confirm your MCO account!",
            "space_add" : "new space add",

    }[category]

def get_template_(category,author):
    return {"space_progress"  : author+"/space_progress_email",
            "space_status_change" : author+"/space_status_change",
            "space_status_complete" : author+"/space_status_complete",
            "space_cityadd" : author+"/space_cityadd",
            "enquiry_space" : author+"/enq_space",
            "enquiry_reply" : author+"/enq_reply",
            "enquiry_status" : author+"/enq_status",
            "enquiry_closed" : author+"/enq_closed",
            "enquiry_accept" : author+"/enq_accept",
            "enquiry_reject" : author+"/enq_reject",
            "enquiry_created" : author+"/enq_created",
            "enquiry_noreply" : author+"/enq_noreply",
            "book_new" : author+"/book_new",
            "book_accept" : author+"/book_accept",
            "book_reject" : author+"/book_reject",
            "book_reminder" : author+"/book_reminder",
            "book_cancel" : author+"/book_cancel",
            "book_cancel_approve" : author+"/book_cancel_approve",
            "book_cancel_disapp" : author+"/book_cancel_disapp",
            "book_incomp_reminder": author +"/book_incomp_rem",
            "book_receipt" : author +"/book_receipt",
            "book_invite" : author +"/book_invite",
            "book_meet_cancel" : author +"/book_meet_cancel",
            "book_noreply" : author +"/book_noreply",
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
            "change_password" : author + "/change_password",
            "forgot_password" : author + "/forgot_password",
            "invite_referral" : author + "/invite_referral",
            "new_booking" : author + "/change_password",
            "signup" : author + "/signup",
            "space_add" : author + "/space_add",

    }[category]

dict1 = {'name': 'Zeba', 'email': 'zebadhongre8@gmail.com'};
dict2 = {'name': 'Leena', 'email': 'leenakhote23@gmail.com'};

booking_summary= {'book_id':'#111', 'book_date':'29 September 2015', 'title':'Desk', 'unit_price':'399.00 INR', 'quantity':'2', 'total':'798.00 INR', 'book_total': '798.00 INR'}
space_user_details= {'name':'MCO ADMIN', 'email':'hello@mycuteoffice.com', 'pay_method':'Online payment', 'space':'Affordable deskspace in Charkop', 'book_type':'Daily', 'start':'15/10/2015', 'end':'16/10/2015', 'duration':' 15/10/2015 to 16/10/2015', 'link': 'https://mycuteoffice.com'}
billing_address= {'name':'MCO ADMIN', 'city':'Mumbai', 'state':'Maharashtra', 'phone':'9821804409'}

space_seeker= {'space_id':'#111', 'enq_id':'12345', 'req_id':'10000000', 'book_id':'200', 'due_date':'10 Sep 2015', 'msg':'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'link':'https://mycuteoffice.com/spaces/cabin'};
admin= {'name':'Admin', 'space_id':'1234', 'book_id':'#0000', 'enq_id':'#99999', 'msg':'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'}
details= {'name':'XYZ', 'contact':'9876543212', 'email':'xyz@gmail.com', 'user_industry':'Dont Know', 'to_date':'1/1/2011', 'from_date':'1/4/2010', 'to_time':'2.30pm', 'from_time':'11am', 'facility':'AC, Internet'}
common= {'name':'XYZ', 'space_id':'1234', 'link':'https://mycuteoffice.com/spaces/cabin'}
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

@app.route("/")
def hello():
    name= "leena"
    author = "common"
    category = "signup"
    subject = get_subject(category)
    template_name = get_template_(category,author)
    recipient = ["dhongre.zeba@gmail.com"]
    generate_email(category=category, name=dict1, template_name=template_name, subject=subject, recipient=recipient, sender="hello@mycuteoffice.com", book_summary= booking_summary, billing_address= billing_address, sud= space_user_details, space_seeker= space_seeker, admin=admin, details=details, common=common)
    return render_template("template25.html", name= name)


if __name__ == "__main__":
    app.run(debug=True)
