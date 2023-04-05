#!/usr/bin/python3
'''script'''

from flask import Flask

app = Flask(__name__)
'''doc'''
@app.route('/')
def route()
    return 'Hello HBNB!'
'''module'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)