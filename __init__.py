from flask import Flask, render_template
from app import configure_routes

def create_app():
    app = Flask(__name__)
    configure_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
