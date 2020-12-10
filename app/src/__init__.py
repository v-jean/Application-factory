from flask import Blueprint

#to work with blueprint before creating an instance app
main_bp = Blueprint("main", __name__)

from . import views, errors