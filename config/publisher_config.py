__author__ = 'zeba'


def get_msg(sender, recipient):
    author = "space_provider"
    category = "book_new"
    subject = "book_new"

    msg = {"sender": sender, "recipient": recipient, "author": author, "category": category,
            "subject": subject, "email_content": get_template_content(subject)
        }

    return msg


def get_template_content(subject):
       return { "Status of Booking ID: Accepted" : {"name" : "leena" ,"space_id" :"12345" ,"book_id" : "34"} ,
                "enquiry_reply" :{"name" : "hello" , "date" : "12345678"},
                "space_progress" : {"name" : "Zeba Dhongre"},
                "forgot password" : {"name" : "MCO" , "link" : "www.google.com"},
                "book_new" : {"name" : "lee" ,"space_id" :"675" ,"user_name" : "leena_khote" , "user_industry" : "mco" ,
                              "space_type" : 'cabin' ,"from_date" :"10/10/2015" , "to_date" :"10/10/2016" , "from_time" : "10 am" ,
                              "to_time" : "8 pm" , "facility" : "all"} ,

       }[subject]