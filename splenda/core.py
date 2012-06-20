# -*- coding: utf-8 -*-

import os


import requests

from flask import Flask, render_template

from flask_heroku import Heroku
from flask_sslify import SSLify
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET', 'some-secret-key')
app.debug = 'DEBUG' in os.environ

# Bootstrap Heroku environment variables.
heroku = Heroku(app)

# Redirect urls to https
sslify = SSLify(app)

# Setup error collection
sentry = Sentry(app)


@app.route('/')
def index():
    r = requests.get('http://travis-ci.org/repositories.json')
    builds = r.json

    return render_template('index.html', builds=builds)

@app.route('/<user>/<repo>')
def repo(user, repo):
    r = requests.get('http://travis-ci.org/{0}/{1}.json'.format(user, repo))
    repo = r.json

    r = requests.get('http://travis-ci.org/{0}/{1}/builds.json'.format(user, repo))
    builds = r.json

    return render_template('repo.html', repo=repo, builds=builds)