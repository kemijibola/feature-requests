from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os, config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'user.login'

def create_app(config):
    # create application instance
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config)
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # register all blueprints here
    from .dashboard import dashboard as dashboard_blueprint
    from .client import client as client_blueprint
    from .account import account as user_account_blueprint

    app.register_blueprint(dashboard_blueprint,url_prefix='/',static_folder='static', static_url_path='__name__')
    app.register_blueprint(client_blueprint, url_prefix='/clients',static_folder='static', static_url_path='__name__')
    # app.register_blueprint(user_account_blueprint)

    return app
