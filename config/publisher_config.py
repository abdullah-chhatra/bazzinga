__author__ = 'zeba'


def get_msg(sender, recipient):
    author = "space_provider"
    category = "feedback_space"
    subject = "Review the space user ID:"

    msg = {"sender": sender, "recipient": recipient, "author": author, "category": category,
            "subject": subject, "email_content": get_template_content(subject)
        }

    return msg


def get_template_content(subject):
       return { #common Templates
                "Your password has been changed" :{"name" : "Zeba Dhongre", "user_name" : "zeba", "link": "https://www.google.com"},
                "Password reset request" :{"name" : "Zeba Dhongre", "link": "https://www.google.com"},
                "Earn Rs. 300 in My Cute Office credit" :{"name" : "Zeba Dhongre", "link1": "https://www.google.com", "link2": "https://www.google.com", "link3": "https://www.google.com", "link4": "https://www.google.com", "ref_code":"1234"},
                "Confirm your MCO account" :{"name" : "Zeba Dhongre", "link": "https://www.google.com"},
                "Space Status change mail" :{"name" : "Zeba Dhongre", "space_id":"#1234", "link": "https://www.google.com"},
                "New spaces matching your requirement" :{"name" : "Zeba Dhongre"},
                "Youre just _ away from completing your booking" :{"name" : "Zeba Dhongre", "percent":"99", "link": "https://www.google.com"},
                #Admin Templates
                "Approval awaiting for Space ID: " :{"name" : "Zeba Dhongre", "space_id":"1099"},
                "Space ID: has been revoked " :{"name" : "Zeba Dhongre", "space_id":"1099", "msg":"Lorem Ipsum is simply dummy text of the printing and typesetting industry"},
                "Enquiry status for Enquiry ID Accepted" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"0909"},
                "Enquiry status for Enquiry ID Rejected" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"0909"},
                "Enquiry ID has exceeded 48 hours without a reply" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"0909"},
                "Booking ID: has been created" :{"name" : "Zeba Dhongre", "book_id":"1099", "contact":"9867898765", "email":"xyz@gmail.com", "user_industry":"ABCD", "space_id":"#123", "from_date":"01/02/2015", "to_date":"30/02/2015", "from_time":"8am", "to_time":"8pm", "facility":"AC, Internet"},
                "Booking confirmation for booking ID: overdue" :{"name" : "Zeba Dhongre", "book_id":"1099", "space_id":"0909"},
                "Request to cancel the booking ID:" :{"name" : "Zeba Dhongre", "book_id":"1099", "space_id":"0909"},
                "Booking ID: has been Accepted" :{"name" : "Zeba Dhongre", "book_id":"1099"},
                "Booking ID: has been Rejected" :{"name" : "Zeba Dhongre", "book_id":"1099"},
                #Space Seeker Templates
                "Your enquiry for space ID:" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"#AC789"},
                "Your enquiry (Enquiry ID: ) has been accepted by the space provider" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"#AC789"},
                "Your enquiry (Enquiry ID: ) has been rejected by the space provider" :{"name" : "Zeba Dhongre", "space_id":"1099", "enq_id":"#AC789"},
                "Your requirement with the ID: is generated." :{"name" : "Zeba Dhongre", "req_id":"1099", "msg":"Lorem Ipsum is simply dummy text of the printing and typesetting industry"},
                "Spaces matching your Requirement ID:" :{"name" : "Zeba Dhongre"},
                "Spaces matching your requirement recently added on MyCuteOffice.com" :{"name" : "Zeba Dhongre"},
                "Status of Booking ID: - Incomplete" :{"name" : "Zeba Dhongre", "book_id":"1234", "link":"https://www.google.com"},
                "Booking Receipt for Booking ID:" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887", "enq_id":"09856"},
                "Status of Booking ID: Accepted" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887"},
                "Status of Booking ID: Rejected" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887"},
                "Booking reminder (Booking ID:)" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887", "due_date":"07 oct 2015"},
                "Review the Space ID:" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887"},
                "Feedback about the system" :{"name" : "Zeba Dhongre"},
                "Your request to cancel booking ID:" :{"name" : "Zeba Dhongre", "book_id":"1234", "space_id":"9887"},
                "Cancel booking approval by the admin" :{"name" : "Zeba Dhongre", "book_id":"1234"},
                "Cancel booking disapproval by the admin" :{"name" : "Zeba Dhongre", "book_id":"1234"},
                #space provider Templates
                "Booked a space / conference room through MyCuteOffice.com? Review us." :{"name" : "Zeba Dhongre"},
                "Review the space user ID:" :{"name" : "Zeba Dhongre", "uid":"AB34", "space_id":"#9887"},

       }[subject]