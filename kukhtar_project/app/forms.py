# відповідні імпорти класів  і полів форм, валідаторів
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

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
