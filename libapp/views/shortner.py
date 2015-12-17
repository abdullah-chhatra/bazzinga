
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
    data = {'url': "https://mycuteoffice.com/spaces/Thane--Maharashtra--India?lat=19.2183307&lng=72.97808970000006&sort=distance&geolocation=Thane%2C%20Maharashtra%2C%20India"}
    res = requests.post("http://localhost:9001/s", data=json.dumps(data))
    if res.ok:
        payload = json.loads(res.content)
    else:
        payload = {"url": "NOT FOUND", "revoke":"FU"}
    return render_template("index.html", payload=payload)


@app.route('/s', methods=['POST'])
def shorten():
    payload = json.loads(request.data)
    body = payload['body']
    data = body['data']
    url = str(data['url']).strip()
    #url = str(payload['url']).strip()

    if not valid_url(url):
        payload['body'] = {"status": "error", "message": "Not a valid URL: {}".format(str(url,))}
        payload['header'] = {"message": "Invalid URL", "status": "error",
                             "token": payload['header']['token']}
        return jsonify(payload, 400)
        #return jsonify({'error': str(url,)}, 400)

    try:
        key, token = shortnerd.insert(url)
        url = url_for('bounce', key=key, _external=True)
        revoke = url_for('revoke', token=token, _external=True)

        payload['body'] = {"message": "Successfully created short url", "status": "success"}
        payload['body']['results'] = {'key': key, 'url': url, 'token': token, 'revoke': revoke}
        payload['header'] = {"message": "Successfully executed command", "status": "success",
                             "token": payload['header']['token']}
        return jsonify(payload)
        #return jsonify({'key': key, 'url': url, 'token': token, 'revoke': revoke})
    except Exception as e:
        payload['body'] = {"status": "error", "message": "{}".format(e)}
        payload['header'] = {"message": "Execution error", "status": "error",
                             "token": payload['header']['token']}
        return jsonify(payload, 400)
        #return jsonify({'error': e}, 400)


@app.route('/s/<key>', methods=['GET'])
def bounce(key):
    try:
        uri = shortnerd[key]
        return redirect(iri_to_uri(uri))
    except KeyError as e:
        return redirect("https://mycuteoffice.com/not-found")
        #return jsonify({'error': 'url not found'}, 400)


@app.route('/r/<token>', methods=['POST'])
def revoke(token):
    payload = {}
    try:
        shortnerd.revoke(token)
        payload['body'] = {"message": "Successfully removed short url", "status": "success"}
        payload['header'] = {"message": "Successfully executed command", "status": "success"}
        return jsonify(payload)
    except Exception as e:
        payload['body'] = {"status": "error", "message": "{}".format(e)}
        payload['header'] = {"message": "Execution error", "status": "error"}
        return jsonify(payload)
        #return jsonify({'error': e}, 400)