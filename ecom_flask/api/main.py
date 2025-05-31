# Main API logic script; here create your endpoints with routes and return values.
from flask import render_template, request, Blueprint, url_for, jsonify
import flask_login

apiBlueprint = Blueprint("main", __name__)


@apiBlueprint.route("/get-product-list/<apiKey>")
def getListOfProducts(apiKey):
    return jsonify("Skibidi Toilet!!!!!!!!")