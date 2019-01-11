from app import db
from . import product
from flask import (render_template, request, redirect, url_for, flash,
                   make_response, session, current_app)

@product.route('/')
def index():
    return render_template('products.html')
