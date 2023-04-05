#!/usr/bin/python3
"""docu"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
    """docu"""
def route()
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
    """docu"""
def routeX()
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)