from flask import Blueprint

dashboard = Blueprint('dashboard',__name__,template_folder='Templates')
from . import view