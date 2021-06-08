from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


login_manager = LoginManager()
# login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message_category = 'info'

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)
    db.create_all(app)
	