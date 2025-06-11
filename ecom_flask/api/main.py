# Main API logic script; here create your endpoints with routes and return values.
from flask import render_template, request, Blueprint, url_for, jsonify
import flask_login
import json
from dotenv import load_dotenv
import os

# Load up environment variables for configuration
load_dotenv()

apiBlueprint = Blueprint("api", __name__)


# Example of a GET request
@apiBlueprint.route("/get-product-list/<apiKey>", methods=["GET"])
def getListOfProducts(apiKey):
    
    products_path = os.path.join(os.path.dirname(__file__), "products.json")
    
    with open(products_path, "r") as f:
        products_data = json.load(f)
        
    return jsonify(products_data)


getListOfProducts('test-key')