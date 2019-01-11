from app import db,ma
from datetime import datetime
from app.BaseMixin import BaseMixin
from app.product.model import Product
from sqlalchemy.orm import validates
from app.client.model import Client
from app.product.model import Product

products = db.Table('products',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

class Feature(db.Model,BaseMixin):
    __tableName__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'),
        nullable=False)
    title = db.Column(db.String(60), index=True, nullable=False)
    description = db.Column(db.Text,nullable=False)
    priority = db.Column(db.Integer,nullable=False)
    target_date = db.Column(db.DateTime,nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

@validates('client_id')
def validate_client_id(self, key, client_id):
    if not client_id:
        raise AssertionError('Please select a client for operation.')

    client = Client.query.filter_by(Client.id == client_id).first()
    if not client:
        raise AssertionError('No such client.')
    return client_id

@validates('title')
def validate_username(self, key, title):
  if not title:
      raise AssertionError('Please provide a title.')

  if len(title) < 3 or len(title) > 60:
    raise AssertionError('Title must be between 3 and 60 characters.')

  return title

@validates('priority')
def validate_priority(self, key, priority, client_id):
    if not priority:
        raise AssertionError('Please provide priority for this feature.')

    if priority < 1 or priority > 100:
        raise AssertionError('Priority must be between range 1 - 100.')
        
    priority_exist = Feature.query.filter_by(Client.id == client_id and Feature.priority == priority).first()
    if priority_exist:
        raise AssertionError('Priority already exist for client.')

    return priority
    
@validates('target_date')
def validate_target_date(self, key, target_date):

    if not target_date:
        raise AssertionError('Please provide valid date time')

    current_date = datetime.utcnow
    if current_date < target_date:
        raise AssertionError('Please provide a valid date.')

    return target_date
    
@validates('product_id')
def validate_product_id(self, key, product_id):
    if not product_id:
        raise AssertionError('Please select product')
        
    product = Product.query.filter_by(Product.id == product_id).first()
    if not product:
        raise AssertionError('Please provide a valid product')

    return product_id

    
