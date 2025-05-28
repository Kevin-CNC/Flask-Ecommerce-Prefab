# Create and return new pre-configured 'Config' class to then attach to main application.
# Basically modularizing the application's configurations.
from flask_caching import Cache
from dotenv import load_dotenv
import os

# Load up environment variables for configuration
load_dotenv()

# Custom configurations, to switch around / add / take out whenever you like
class App_Configurations:
    DEBUG = False
    SECRET_KEY = os.getenv('my_secret_key')
    STRIPE_SECR_KEY = os.getenv('stripe_secret_key')
