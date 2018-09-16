from flask import Flask, g
from flask.ext.login import LoginManager

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = "asldfjalkghhgwiuerqhgjkdhnaasjdfhsalkfaubg"

login_manager = LoginManager()
login_manager.init_app(app) # sets up the login manager for our app
login_manager.login_view = 'login' # if not logged in, redirect them to the login view

# function for login_manager to use to lookup a User
@login_manager.user_loader
def load_user(userid):
    try: # retrieve record from the db
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist: # no record found
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE # set the database as global
    g.db.connect() # ensure a global db connection

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close() # close global db connection
    return response

if __name__ == '__main__':
    models.initialize() # initialize db
    models.User.create_user( # create a dummy user using create_user to encrypt password
            name="Jake",
            email="schroeder.marketing@outlook.com",
            password="password",
            admin=True
            )
    app.run(debug=DEBUG, host=HOST, port=PORT)
