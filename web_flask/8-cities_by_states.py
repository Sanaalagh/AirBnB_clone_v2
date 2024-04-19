#!/usr/bin/python3
"""
Script to start a Flask web application that displays states and their cities.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """Route to display states and their associated cities."""
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Teardown method to close the database session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
