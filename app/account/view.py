from app import db
from . import account
from flask import (render_template, request, redirect, url_for, flash,
                   make_response, session, current_app)

@account.route('/')
def index():
    return render_template('login.html')

@account.route('/register')
def register():
    return render_template('registration.html')
