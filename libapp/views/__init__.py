__author__ = 'rahul'


from flask import render_template
from .. import app
from ..publisher import publish_msg
from ..subscriber import subscribe_data
from ..config import libconf


@app.route("/")
def index():
    subscribe_data.apply_async(queue=libconf.EMAIL_Q, serializer='json')
    return render_template("index.html")


@app.route("/publisher")
def publisher():
    publish_msg()
    return render_template("publisher.html")