# відповідні імпорти класів  і полів форм, валідаторів
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Regexp, DataRequired, Length, Email, EqualTo, ValidationError
from .models import Task, Category, User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

#Імплементувати контактну форму
class TaskForm(FlaskForm):
	title = StringField('Назва ', validators=[DataRequired()])
	description = StringField('Опис ', validators=[DataRequired()])
	created = StringField('Дата створення ')
	is_done = StringField('Закінчена ')
	priority = SelectField('Пріорітетність ', choices=[
    	("low", "low"), 
    	("medium", "medium"), 
    	("high", "high")]) 
	categories = SelectField(u'Категорії')


class CategoryForm(FlaskForm):
	name = StringField('Назва ', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators=[Length(min=4, max=25,
		message = 'Це поле має бути довжиною між 4 та 25 символів'),
		DataRequired(message = 'Це поле обов\'язкове'),
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0, 'Username must have only letters numbers dots')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password',
		validators=[Length(min=6,message='Це поле має бути більше 6 символів'),
		DataRequired(message = 'Це поле обов\'язкове')])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')


	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already registered.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', 
		validators=[Length(min=4, max=25,
		message = 'Це поле має бути довжиною між 4 та 25 символів')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')


	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already registered.')