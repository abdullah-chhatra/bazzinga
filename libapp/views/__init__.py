__author__ = 'rahul'


from flask import render_template
from .. import app
from ..publisher import publish_msg, send_sms, subscribe_msg
#from ..sender import publish_msg, subscribe_msg, send_sms
from ..tasks import subscribe_data
from ..config import libconf


@app.route("/")
def index():
    subscribe_data.apply_async(queue=libconf.EMAIL_Q, serializer='json')
    return render_template("index.html")


@app.route("/publisher", methods=["GET", "POST"])
def publisher():
    publish_msg(source_q=libconf.PUB_EMAIL_Q, dest_q=libconf.EMAIL_Q) #.apply_async(serializer='json')
    return render_template("publisher.html")


@app.route("/sms", methods=["GET", "POST"])
def sms():
    send_sms()
    return render_template("index.html")