# відповідні імпорти класів  і полів форм, валідаторів
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

#Імплементувати контактну форму
class Form(FlaskForm):
	name = StringField('Name: ', validators=[DataRequired()])
	email = StringField('email: ', validators=[DataRequired()])
	message = StringField('message: ', validators=[DataRequired()])

