from ..models import *
from . import main_bp
from .. import db
from flask import render_template, request, session, redirect, flash, url_for

#routes
@main_bp.route('/')
def home():
    return render_template('home.html')