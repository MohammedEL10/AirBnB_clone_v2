#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def Hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb/')
def hello():
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """replace text with variable."""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
