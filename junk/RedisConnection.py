import os
import redis

from flask import Flask, render_template
from flask import Response
from flask import json
import pickle

app = Flask(__name__)
app.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/test.json")
def dict_to_redis_hset():
    data = pickle.loads(app.redis.get("test1"))
    x = data['receiver']
    for index in range(len(x)):
        y = x[index]
        print 'Current name :', x[index]
        resp = Response(y, status= 200, mimetype='application/json')
    return resp

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
  port = int(os.getenv('PORT', 5000))
  app.run(host='localhost', port=port, debug=True)