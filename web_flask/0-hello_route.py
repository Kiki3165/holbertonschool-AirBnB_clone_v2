#!/usr/bin/python3
'''script'''

from flask import Flask

'''doc'''

app = Flask(__name__)

@app.route('/', strict_slashes=False')
    '''def route'''
    def route()
        return 'Hello HBNB!'

'''module'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)