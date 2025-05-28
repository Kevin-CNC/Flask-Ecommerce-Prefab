# This is the script which will return the finilazed web application to the main script.
# Will be using blueprints and other modules to define how each section of the backend should react (eg: routes, api endpoints, etc...)
from flask import Flask
from flask_compress import Compress
from configurations import C_Configurations
import os

Compressor = Compress()

def init_application():
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static-files")
    
    main_app = Flask(__name__,static_folder=static_dir)
    main_app.config.from_object(C_Configurations)
    
    Compressor.init_app(main_app)
    
    return main_app