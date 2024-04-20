#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():

    """return some text"""
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def HBNB():

    """return some text"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):

    """return some text"""
    return "C is %s" % text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
