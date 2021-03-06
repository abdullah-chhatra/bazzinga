__author__ = 'rahul'

from flask import Flask

def create_app():
    """
    Create app and configure the details
    :rtype : object
    """
    from .config import libconf, celconf
    app = Flask(__name__, template_folder=libconf.TEMPLATE_DIR, static_folder=libconf.STATIC_PATH, static_url_path="")
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')

    # Configure app
    # app.config.from_object(settings)

    return app


def init_app(app):
    """
    Initializes app with needed configurations for add-on entities
    """
    from .init import loggerd, celeryd, redisd, shortnerd

    loggerd.init_app(app)
    celeryd = celeryd.init_app(app)
    redisd, pubsubd = redisd.init_app(app)
    shortnerd = shortnerd.init_app(app)

    return celeryd, redisd, pubsubd, shortnerd


app = create_app()
celeryd, redisd, pubsubd, shortnerd = init_app(app)

from views import *