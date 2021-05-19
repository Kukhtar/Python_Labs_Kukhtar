from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import config
# db.init_app(app)
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)
app.config.from_object('config') #налаштування з файлу config.py

from app import views
from app.models import db


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
