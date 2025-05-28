# This is the script which will return the finilazed web application to the main script.
# Will be using blueprints and other modules to define how each section of the backend should react (eg: routes, api endpoints, etc...)
from flask import Flask
from flask_compress import Compress
from flask_caching import Cache
from configurations import App_Configurations
import os

AppCompressor = Compress()
AppCache = Cache(config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 3600  #in seconds
})

def init_application():
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static-files")
    
    app = Flask(__name__,static_folder=static_dir)
    app.config.from_object(App_Configurations)

    AppCache.init_app(app) # Initialize application's cache methods
    AppCompressor.init_app(app) # Initialize application's JSON request methods
    
    return app