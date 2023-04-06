#!/usr/bin/python3
"""docu"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """Display a list of all State objects sorted by name"""
    states = storage.all('State')
    states_sorted = sorted(states.values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
