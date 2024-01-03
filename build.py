from flask_frozen import Freezer
from __init__ import create_app

# Monkey-patch Flask to work with Frozen-Flask
import flask
from werkzeug.wrappers import Response

flask.Flask.response_class = Response

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()

# Create an instance of Freezer for generating the static files from
# the Flask application routes
freezer = Freezer(app)

if __name__ == '__main__':
    # Generate the static files using Frozen-Flask
    freezer.freeze()