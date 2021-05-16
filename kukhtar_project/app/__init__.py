from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import config
db=SQLAlchemy()
# db.init_app(app)
app = Flask(__name__)
app.config.from_object('config') #налаштування з файлу config.py

from app import views
