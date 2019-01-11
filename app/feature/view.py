from app import db
from . import feature
from flask import (render_template, request, redirect, url_for, flash,
                   make_response, session, current_app)

@feature.route('/')
def index():
    return render_template('features.html')
