# Create main paths blueprints for the application.
# Not much logic behind it apart from rendering pages.
from flask import render_template, request, Blueprint

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/about", methods=["GET"])
def about():
    return render_template("about.html")