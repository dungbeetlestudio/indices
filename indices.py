
#!/usr/bin/env python
import copy
import json
import os
from datetime import datetime
from flask import Flask, abort, redirect, request, url_for
from gevent import pywsgi

app = Flask(__name__,'')

@app.route('/indices-realtime')
def status():
    data = []
    try:
        name = request.args['name']
        with open(f'db/indices/{name}/{datetime.today().date()}.json') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(e)
    return { 'val':data, 'err':None }

print('http://localhost:8888/indices-realtime')
http_server = pywsgi.WSGIServer(('0.0.0.0', 8888), app)
http_server.serve_forever()
