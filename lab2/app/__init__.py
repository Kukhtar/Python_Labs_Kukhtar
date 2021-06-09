from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
# from .extensions import db, login_manager
app = Flask(__name__)
app.config.from_object('config') #налаштування з файлу config.py

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message_category = 'info'

# from app.extensions import db
db = SQLAlchemy(app)
from app import views


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
