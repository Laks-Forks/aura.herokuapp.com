from flask import Blueprint

stack = Blueprint('stack', __name__)

from . import views