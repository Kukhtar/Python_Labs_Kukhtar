from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.String)
	created = db.Column(db.DateTime, default=datetime.utcnow)
	is_done = db.Column(db.Boolean, default = False)
	priority = db.Column(db.String, default = 'low')

	def __repr__(self):
		return '<Agreement %r>' % self.id 