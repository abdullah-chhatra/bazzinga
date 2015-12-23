
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
    '''
    data = {}
    data['header'] = {'token': ""}
    data['body'] = {}
    data['body']['data'] = {'url': "https://mycuteoffice.com", "type": "s"}
    res = requests.post("http://localhost:9001/shorten", data=json.dumps(data))
    if res.ok:
        payload = json.loads(res.content)
    else:
        payload = {"url": "NOT FOUND", "revoke":"NOT POSSIBLE"}
    '''
    return render_template("index.html")  #, payload=payload)


@app.route('/shorten', methods=['POST'])
def shorten():
    payload = json.loads(request.data)
    body = payload['body']
    data = body['data']
    url = str(data['url']).strip()
    id_type = str(data['type']).strip()

    if not valid_url(url):
        payload['body'] = {"status": "error", "message": "Not a valid URL: {}".format(str(url,))}
        payload['header'] = {"message": "Invalid URL", "status": "error",
                             "token": payload['header']['token']}
        return jsonify(payload, 400)

    try:
        key, token = shortnerd.insert(url)
        url = url_for('bounce', id_type=id_type, key=key, _external=True)
        revoke = url_for('revoke', token=token, _external=True)

        payload['body'] = {"message": "Successfully created short url", "status": "success"}
        payload['body']['results'] = {'key': key, 'url': url, 'token': token, 'revoke': revoke}
        payload['header'] = {"message": "Successfully executed command", "status": "success",
                             "token": payload['header']['token']}
        return jsonify(payload)
    except Exception as e:
        payload['body'] = {"status": "error", "message": "{}".format(e)}
        payload['header'] = {"message": "Execution error", "status": "error",
                             "token": payload['header']['token']}
        return jsonify(payload, 400)


@app.route('/<id_type>/<key>', methods=['GET'])
def bounce(id_type, key):
    query_string = request.query_string
    try:
        uri = shortnerd[key]
        redirect_url = "{url}?{query}".format(url=iri_to_uri(uri), query=query_string)
        return redirect(redirect_url)
        #return redirect(iri_to_uri(uri))
    except KeyError as e:
        return redirect("https://mycuteoffice.com/not-found")


@app.route('/revoke/<token>', methods=['POST'])
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