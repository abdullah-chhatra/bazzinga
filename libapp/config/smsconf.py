from enum import Enum

HOST                     = "http://mobicomm.dove-sms.com"
USERNAME                 = "Mycute"
KEY                      = "ac85166574XX"

HTTP_ENDPOINT            = "/submitsms.jsp"
XML_ENDPOINT             = "/submitsms.jsp"
DELIVERY_REPORT_ENDPOINT = "/getreport.jsp"

UNICODE                  = "no"

# status messages
SENDERID                 = Enum("Senderid", "OFFICE, alertsp, alertsi")
ACCUSAGE                 = Enum("Accusage", "trans, promo, international")
SMSTYPE                  = Enum("smstype", "normal, flash")


# ignore key list and delete key list
IGNORE_KEYS = ["message_content"]
DELETE_KEYS = ["msg_type", "author", "category", "template"]


"""
URL:- http://mobicomm.dove-sms.com
Username:-Mycute
Password:-M&a789
Service:-PT,T
Client Code:-19924
"""