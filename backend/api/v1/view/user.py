#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify
from models.user import User
from models import storage

user = Blueprint('user', __name__)

@user.route('/', methods=['GET', 'POST'])
def hello():
    return jsonify({'message': 'From user route'})

@user.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    """Login route"""
    return jsonify({'message': 'Successfully logged in'})


@user.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    """Register route"""
    return jsonify({'message': 'Successfully registered'})