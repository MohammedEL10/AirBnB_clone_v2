#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/hbnb/', strict_slashes=False)
def HBNB():


    """return some text"""
    return "HBNB"
@app.route(/c/<text>, strict_slashes=False)
def text():
    

    """return some text"""
    return "C"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
