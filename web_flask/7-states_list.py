#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects from the storage"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
