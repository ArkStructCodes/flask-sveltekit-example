from flask import Blueprint, Flask
from . import random


def register_blueprint(app: Flask, blueprint: Blueprint) -> None:
    blueprint.static_folder = app.static_folder
    blueprint.static_url_path = app.static_url_path
    app.register_blueprint(blueprint)
    

def create_app() -> Flask:
    app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

    @app.route("/")
    def page():
        return app.send_static_file("index.html")

    # This enables sending arbitrary static files, like CSS, JS, images etc.
    @app.route("/<path:path>")
    def static_files(path):
        return app.send_static_file(path)

    register_blueprint(app, random.blueprint)
    return app
