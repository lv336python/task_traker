"""
The users Blueprint handles the user management for this application.
Specifically, this Blueprint allows for new users to register and for
users to log in and to log out of the application.
"""
from flask import Flask
from flask import Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

app = Flask(__name__)

from app import routes
