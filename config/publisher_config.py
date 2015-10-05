__author__ = 'zeba'


def get_msg(sender, recipient):
    author = "space_provider"
    category = "space_progress"
    subject = "space_progress"

    msg = {"sender": sender, "recipient": recipient, "author": author, "category": category,
            "subject": subject, "email_content": get_template_content(subject)
        }

    return msg


def get_template_content(subject):
       return { "Status of Booking ID: Accepted" : {"name" : "leena" ,"space_id" :"12345" ,"book_id" : "34"} ,
                "enquiry_reply" :{"name" : "hello" , "date" : "12345678"},
                "space_progress" : {"name" : "Zeba Dhongre"}
       }[subject]