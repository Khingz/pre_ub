#!/usr/bin/env python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask
from .view.user import user
from models.user import User
from models import storage
import os

# Get env variables
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


app.register_blueprint(user, url_prefix='/api/v1/user')