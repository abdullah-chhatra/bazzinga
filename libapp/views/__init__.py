__author__ = 'rahul'


from flask import render_template
from .. import app
from ..subscriber import subscribe_data
from ..publisher import publish_msg
from junk.email_task import send_email

@app.route("/")
def index():
    send_email.delay()
    #subscribe_data()
    return render_template("index.html")


@app.route("/publisher")
def publisher():
    publish_msg()
    return render_template("publisher.html")