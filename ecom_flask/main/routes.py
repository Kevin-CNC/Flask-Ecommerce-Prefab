# Create main paths blueprints for the application.
# Not much logic behind it apart from rendering pages.
from flask import render_template, request, Blueprint

mainRoutesBlueprint = Blueprint("main", __name__)

@mainRoutesBlueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@mainRoutesBlueprint.route("/about", methods=["GET"])
def about():
    return render_template("about.html")