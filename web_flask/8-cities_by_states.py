#!/usr/bin/python3
""" Starts a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of States and Cities"""
    states = storage.all(State).values()
    cities = list()
    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('8-cities_by_states.html',
                           states=states, state_cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
