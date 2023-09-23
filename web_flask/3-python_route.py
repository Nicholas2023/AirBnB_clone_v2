#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when accessing the root URL
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when accessing the '/hbnb' URL
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """
    Displays 'C' followed by the value of the variable
    """
    return "C " + escape(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python' followed byt he value of the text variable
    """
    return "Python " + escape(text.replace("_", " "))


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000)
