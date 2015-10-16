__author__ = 'rahul'


from flask import render_template
from .. import app
from ..publisher import publish_msg
from ..email_task import send_email
from libapp.subscriber import subscribe_data


@app.route("/")
def index():
    send_email.delay()
    #subscribe_data()
    return render_template("index.html")


@app.route("/publisher")
def publisher():
    publish_msg()
    return render_template("publisher.html")