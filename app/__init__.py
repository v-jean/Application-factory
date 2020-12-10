from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_name

db = SQLAlchemy()

#Application factory function
def create_app(mode_config_name):
    app = Flask(__name__)
    app.config.from_object(config_name[mode_config_name])
    app.template_folder = "html"

    db.init_app(app)

    from .src import main_bp as mbp
    app.register_blueprint(mbp)

    return app