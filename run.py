import os
from app import db, create_app
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from app.client.model import Client
from app.product.model import Product
from app.feature.model import Feature


from app import db,create_app

app = create_app(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')
manager = Manager(app)

# @app.shell_context_processor
def make_shell_context():
    return dict(app=app,db=db,Client=Client,Product=Product,Feature=Feature)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


