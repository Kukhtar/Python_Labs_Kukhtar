from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #налаштування з файлу config.py

from app import views
