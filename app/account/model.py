from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from app import BaseMixin

class User(BaseMixin, db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    