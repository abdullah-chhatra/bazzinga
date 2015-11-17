
import time
import dovesoft
from dovesoft.exceptions import DoveSoftClientError
#from libapp import app
import config.smsconf as settings

ds = dovesoft.DoveSoftClient(settings.USERNAME, settings.KEY)


def generate_message(recipients, text_body, sender, category, **opts):
    message = dovesoft.Sms()
    message.set_to(recipients)
    message.set_message(text_body)
    message.set_from(sender)
    message.set_smstype(category)
    message.set_senderid(opts.get('senderid', ''))
    message.set_accusage(opts.get('accusage', ''))
    message.set_time(opts.get('time', ''))
    message.set_unicode(opts.get('unicode_status', False))
    return message


def send_message(message):
    try:
        msg = ds.send(message)
        #app.logger.info("Successfully sent message: {msg}".format(msg=msg))
        return msg
    except DoveSoftClientError as sgce:
        #app.logger.error("Error while sending email: {msg}".format(msg=msg))
        #app.logger.error("Email: {message}".format(message=message))
        raise DoveSoftClientError(sgce.code, sgce.read())


def message_notifier(category, author, sender, recipient, subject, **kwargs):
    message = generate_message(recipients=recipient, text_body=kwargs.get("text", "Rahul: Test sms"),
                               sender=sender, category=category, **kwargs)
    send_message(message)



message_notifier(category=settings.SMSTYPE.normal.name, author="", sender=settings.USERNAME, recipient=9821804409,
                 subject="", text="Test Message", senderid=settings.SENDERID.OFFICE.name,
                 accusage=settings.ACCUSAGE.trans.value)
