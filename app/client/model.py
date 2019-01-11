from app import db, ma, login_manager
from flask_login import UserMixin
from datetime import datetime
from app.BaseMixin import BaseMixin
from sqlalchemy.orm import validates
import re

class Client(db.Model, BaseMixin):
    __tableName__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.BigInteger, unique=True, index=True)
    email = db.Column(db.String(60), unique=True, index=True, nullable=False)
    address1 = db.Column(db.String(128))
    features = db.relationship('Feature', backref='client', lazy=True)

    @validates('fullname')
    def validate_fullname(self, key, fullname):
        if not fullname:
            raise AssertionError('Please provide my fullname.')

        return fullname

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if not phone_number:
            raise AssertionError('Please provide phone number.')
        
        if not re.match("\\d{10}", phone_number):
            raise AssertionError('Please provide a valid phone number.')

        phone_number_exist = Client.query.filter_by(phone_number=phone_number).first()
        if phone_number_exist:
            raise AssertionError('Phone number {} already exist.'.format(phone_number))
        
        return phone_number

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Please provide email.') 
        
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Please provide a valid email.')

        email_exist = Client.query.filter_by(email=email).first()
        if email_exist:
            raise AssertionError('Email address already exist')

        return email