#!/usr/bin/python3
"""docu"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/hbnb_filters')
def hbnb_filters():
    """Display the HTML page like 6-index.html"""
    # Load State, City, and Amenity objects from DBStorage and sort them by name
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    cities = sorted(storage.all("City").values(), key=lambda city: city.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
