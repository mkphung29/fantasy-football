from flask_frozen import Freezer
from __init__ import create_app
import subprocess

# Activate virtual environment
subprocess.run(["python", "-m", "venv", "venv"])
subprocess.run(["source", "venv/bin/activate"])

# Install dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()

# Create an instance of Freezer for generating the static files from
# the Flask application routes 
freezer = Freezer(app)


if __name__ == '__main__':
    # Generate the static files using Frozen-Flask
    freezer.freeze()