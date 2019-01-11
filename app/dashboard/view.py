from app import db
from . import dashboard
from flask import (render_template, request, redirect, url_for, flash,
                   make_response, session, current_app)

@dashboard.route('/')
def index():
    return render_template('dashboard.html')
