import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

#Create app through application factory function
app = create_app(os.getenv("FLASK_CONFIG") or 'default')
#Here the db was initializated with app

manager = Manager(app)
migrate = Migrate(app, db)

shell_context = dict(app=app, db=db, Brand=Brand, Car=Car)

manager.add_command("shell", Shell(make_context=shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()