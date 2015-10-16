__author__ = 'rahul'


from flask import render_template
from .. import app
from ..publisher import publish_msg
from ..subscriber import subscribe_data


@app.route("/")
def index():
    subscribe_data.delay()
    return render_template("index.html")


@app.route("/publisher")
def publisher():
    publish_msg()
    return render_template("publisher.html")