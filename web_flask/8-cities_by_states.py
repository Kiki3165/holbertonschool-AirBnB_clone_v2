#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a HTML page with all cities by state """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
