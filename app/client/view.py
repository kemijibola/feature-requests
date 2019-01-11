from app import db
from . import client
from .model import Client
from app.schema import ClientSchema
from flask_wtf.csrf import CSRFError
from app.decorators import validator
# from app.decorators import validator
from flask import (render_template, jsonify, request, redirect, url_for, flash,
                   make_response, session, current_app, json)

@client.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone_number = request.form['phone_number']
        email = request.form['email']
        address1 = request.form['address1']
        try:
            client = Client()
            client_schema = ClientSchema()
            clients_schema = ClientSchema(many=True)
            client_instance.create(fullname=fullname,phone_number=phone_number,email=email,address1=address1)
            return jsonify(msg='Successfully created', data=Client.id),201
        except AssertionError as exception_message:
            return jsonify(msg='Error: {}. '.format(exception_message)), 400
    return render_template('clients.html')

@client.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400
