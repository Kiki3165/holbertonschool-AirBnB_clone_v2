#!/usr/bin/python3
"""This script starts a Flask web application with two routes"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Close the database"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display a list of all states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a list of all cities in a given state"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-not_found.html'), 404
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-state.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
