#!/usr/bin/env python
# coding: utf-8

import random
import logging
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Innsbruck!'


@app.route('/hallo')
def hello2():
    """
    Gibt einen Json-String zurück
    """
    
    return jsonify({
        "ort": "Innsbruck",
        "land": u"Österreich",
        "plz": 6020,
        "rand": random.randrange(1, 11)
    })


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host = '127.0.0.1', port = 8080, debug = True)
