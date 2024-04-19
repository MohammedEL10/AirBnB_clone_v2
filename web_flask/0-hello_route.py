#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask

""" the app take the model (__name__)"""


app = Flask(__name__)


@app.route("/")
""" define Hello_HBNB """


def Hello_HBNB():
    return "Hello, HBNB"
