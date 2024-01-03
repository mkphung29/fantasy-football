from flask_frozen import Freezer
from __init__ import create_app
import subprocess

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()

# Create an instance of Freezer for generating the static files from
# the Flask application routes
#freezer = Freezer(app)

