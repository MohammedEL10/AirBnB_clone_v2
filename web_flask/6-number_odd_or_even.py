#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask, render_template


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
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/(<text>)')
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    n = str(n)
    return render_template('5-number.html', n=n)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
