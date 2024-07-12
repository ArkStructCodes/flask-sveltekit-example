import random
from flask import Blueprint


blueprint = Blueprint("random", __name__)


@blueprint.route("/api/random")
def random_int():
    return str(random.randint(0, 100))


@blueprint.route("/random")
def page():
    return blueprint.send_static_file("random.html")
