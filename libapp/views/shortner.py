
import requests
import json
from rfc3987 import parse
from shorten import RevokeError
from werkzeug.urls import iri_to_uri

from flask import render_template, request, redirect, url_for
from flask import jsonify as _jsonify

from .. import app, shortnerd


def jsonify(obj, status_code=200):
    obj['status'] = 'error' if 'error' in obj else 'okay'
    res = _jsonify(obj)
    res.status_code = status_code
    return res


def valid_url(url):
    p = parse(url, rule='URI_reference')
    return all([p['scheme'], p['authority'], p['path']])


@app.route('/', methods=['GET', 'POST'])
def index():
    data = {'url': "http://microservices.io/microservices/news/2015/01/15/example-microservice-app.html"}
    res = requests.post("http://localhost:9001/s", data=json.dumps(data))
    if res.ok:
        payload = json.loads(res.content)
    else:
        payload = {"url": "NOT FOUND", "revoke":"FU"}
    return render_template("index.html", payload=payload)


@app.route('/s', methods=['POST'])
def shorten():
    payload = json.loads(request.data)
    url = str(payload['url']).strip()

    if not valid_url(url):
        return jsonify({'error': str(url,)}, 400)

    try:
        key, token = shortnerd.insert(url)
        url = url_for('bounce', key=key, _external=True)
        revoke = url_for('revoke', token=token, _external=True)

        return jsonify({'url': url, 'revoke': revoke})
    except Exception as e:
        return jsonify({'error': e}, 400)


@app.route('/s/<key>', methods=['GET'])
def bounce(key):
    try:
        uri = shortnerd[key]
        return redirect(iri_to_uri(uri))
    except KeyError as e:
        return jsonify({'error': 'url not found'}, 400)


@app.route('/r/<token>', methods=['POST'])
def revoke(token):
    try:
        shortnerd.revoke(token)
    except RevokeError as e:
        return jsonify({'error': e}, 400)