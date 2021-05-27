from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy
from app import login_manager
from flask_login import UserMixin

db = SQLAlchemy(app)


@login_manager.user_loader
def user_loader(user_id):
	return User.query.get(int(user_id))

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.String)
	created = db.Column(db.DateTime, default=datetime.utcnow)
	is_done = db.Column(db.Boolean, default = False)
	priority = db.Column(db.String, default = 'low')
	category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))

	def __repr__(self):
		return '<Agreement %r>' % self

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	tasks = db.relationship('Task', backref='category')

	def __repr__(self):
		return "<{}:{}>".format(id, self.name)


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(60), nullable=False)
	password = db.Column(db.String(60), nullable = False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}'"