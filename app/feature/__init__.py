from flask import Blueprint

feature = Blueprint('feature',__name__,template_folder='Templates')
from . import view