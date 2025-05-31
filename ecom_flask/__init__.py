# This is the script which will return the finilazed web application to the main script.
# Will be using blueprints and other modules to define how each section of the backend should react (eg: routes, api endpoints, etc...)
import os
from flask import Flask
from flask_compress import Compress
from flask_caching import Cache
# For user-made-modules / your custom modules, use relative imports
from .configurations import App_Configurations
from .main.routes import mainRoutesBlueprint
from .errors.routes import errorRoutesBlueprint

AppCompressor = Compress()
AppCache = Cache(config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 3600  #in seconds
})

def init_application():
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static-files")
    pages_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web-pages")
    
    app = Flask(__name__,static_folder=static_dir, template_folder=pages_dir)
    app.config.from_object(App_Configurations)
    
    # Assigning routes to the app
    for blueprint in [mainRoutesBlueprint,errorRoutesBlueprint]:
        app.register_blueprint(blueprint)

    AppCache.init_app(app) # Initialize application's cache methods
    AppCompressor.init_app(app) # Initialize application's JSON request methods
    
    return app