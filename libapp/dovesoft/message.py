

class Sms(object):
    """
    Dove soft message
    """
    def __init__(self, **opts):
        """
        Constructs Dove Soft Message object.

        Args:
            to: Recipient mobile number
            message: SMS body
            time: Set date and time
        """
        self.mobile = opts.get("mobile", "")
        self.message = opts.get("message", "")
        self.senderid = opts.get("senderid", "")
        self.accusage = opts.get("accusage", "")
        self.unicode_status = opts.get("unicode_status", "")
        self.smstype = opts.get("smstype", "")
        self.time = opts.get("time", "")
        self.idno = opts.get("idno", "")

    def set_to(self, to):
        self.mobile = to

    def set_message(self, text):
        self.message = text

    def set_senderid(self, senderid):
        self.senderid = senderid

    def set_accusage(self, accusage):
        self.accusage = accusage

    def set_unicode(self, unicode_status):
        self.unicode_status = unicode_status

    def set_smstype(self, smstype):
        self.smstype = smstype

    def set_time(self, time):
        self.time = time

    def set_idno(self, idno):
        self.idno = idno