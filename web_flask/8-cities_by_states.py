#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_cities_list():
    """
    Displays a list of states and cities.
    """
    states = []
    for state in storage.all(State).values():
        states.append({**state.to_dict(), **{'cities': state.cities}})

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')