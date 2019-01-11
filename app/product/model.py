from app import db,ma
from datetime import datetime
from app.BaseMixin import BaseMixin
from sqlalchemy.orm import validates

class Product(db.Model,BaseMixin):
    __tableName__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

@validates
def validate_name(self, key, name):
    if not name:
        raise AssertionError('Please provide product name')