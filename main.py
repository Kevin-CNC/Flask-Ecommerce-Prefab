from ecom_flask import init_application

# Choose if you'd like to run the application in debug mode or not.
isDebug = True

if __name__ == "__main__":
    app = init_application()
    app.run(debug=isDebug)