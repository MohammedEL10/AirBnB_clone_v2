#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def Hello_HBNB():
    return "Hello HBNB"


@app.route('/hbnb')
def Hello():
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/(<text>)')
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number_text(n):
    n = str(n)
    return '{} in a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
