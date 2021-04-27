from flask import Flask, render_template, url_for, request, flash, redirect
from app import app
import platform, sys
from datetime import datetime
from .forms import Form


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
	# flash('asdasd')
	data = getData()
	f = Form()
	# if f.validate_on_submit():
	# 	flash('asdasd')
	# 	return
	# 	# return redirect(url_for('form'))
	# return render_template('form.html', form=f, pageTitle='Form', data=data)
	if request.method == 'POST':
 		if f.validate_on_submit():
 			flash('You were successfully logged in')
 			return redirect(url_for('form'))
 		else:
 			flash('You were successfully logged in')
 			return redirect(url_for('index'))
	return render_template('form.html', form=f, pageTitle='Form', data=data)
if __name__ == "__main__":
	app.run(debug=True)
