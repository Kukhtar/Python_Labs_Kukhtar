from flask import Flask, render_template, url_for, request
import platform, sys
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY']='asd'

class Form(FlaskForm):
	name = StringField('Name: ', validators=[DataRequired()])
	email = StringField('email: ', validators=[DataRequired()])
	message = StringField('message: ', validators=[DataRequired()])

@app.route('/')
def index():
	data = getData()
	return render_template('index.html', data = data)

@app.route('/about/')
def about():
	data = getData()
	return render_template('about.html', data = data)


skill=["Spring Boot/MVC/WEB/Data", "MongoDB/MySQL/PostgreSql", "HTML/CSS/JS", "Docker", "Postman", "Linux", "Tomcat", "GCP", "Lombok"]
@app.route('/skills/')
def skills():
	data = getData()
	return render_template('skills.html', len = len(skill), skill = skill, data = data)

@app.route('/contact/')
def contact():
	data = getData()
	return render_template('contact.html', data = data)

def getData():
	now = datetime.now()
	return ["User: " + str(request.headers.get('User-Agent')) , "Platform: " + str(platform.system()) + "Python version:" + str(sys.version_info[0]) + "   Time: " + str(now.strftime("%H:%M:%S"))]

@app.route('/form', methods=['GET','POST'])
def form():
	data = getData()
	f = Form()
	if f.validate_on_submit():
		return "<h2> Name: {0}, email: {1}, message: {2}".format(f.name.data, f.email.data, f.message.data)

	return render_template('form.html', form=f, pageTitle='Form', data=data)

if __name__ == "__main__":
	app.run(debug=True)