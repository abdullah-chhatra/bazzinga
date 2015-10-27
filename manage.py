# A test file for python. Actual code will be included in future!
import os
import sys
from flask.ext.script import Manager, Server
from libapp import app
from libapp.config import libconf as settings


host = str(os.environ.get("HOST", settings.HOST))
port = int(os.environ.get("PORT", settings.PORT))
debug = bool(os.environ.get("DEBUG", settings.DEBUG))
threaded = bool(os.environ.get("THREADED", settings.THREADED))

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


manager = Manager(app)

manager.add_command("runserver", Server(host=host, port=port, use_debugger=debug, threaded=threaded, use_reloader=True))


'''
@manager.command
def run_nose():
    nose.run()
'''


if __name__ == "__main__":
    manager.run()