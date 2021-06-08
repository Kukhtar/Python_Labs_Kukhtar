from flask import Flask

from task.views import  tasks_bp
from login.views import  login_bp
from extensions.database import db
from extensions.database import login_manager  
from models import Task,Category


def create_app():
	app = Flask(__name__)
	app.config.from_object('config') #налаштування з файлу config.py
	app.register_blueprint(tasks_bp, url_prefix='/')
	app.register_blueprint(login_bp, url_prefix='/')

	# database.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	return app

if __name__ == "__main__":
	create_app().run(debug=True)
