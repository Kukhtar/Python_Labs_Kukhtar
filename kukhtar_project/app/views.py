from flask import Flask, render_template, url_for, request, flash, redirect
from app import app
import platform, sys
from datetime import datetime
from .forms import TaskForm
from .models import Task
from flask_sqlalchemy import SQLAlchemy
from app.models import db

with app.app_context():
    db.create_all()

@app.route('/')
def index():
	db.create_all()
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

@app.route('/task')
def getall():
	data = getData()
	args = Task.query.all()
	return render_template('getall.html', args = args, len = len(args), data = data)

@app.route('/task/<int:id>')
def getTask(id):
	data = getData()
	args = Task.query.get_or_404(id)
	return render_template('task.html', args = args, data = data)

@app.route('/task/<int:id>/delete')
def delete(id):
	task_to_delete = Task.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect(url_for('getall'))
	except:
		return 'Can\'t delete task'

@app.route('/task/<int:id>/update')
def update(id):
	task_to_delete = Task.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect(url_for('task'))
	except:
		return 'Can\'t delete task'
		
@app.route('/task/create', methods=['POST', 'GET'])
def task():
	data = getData()
	f = TaskForm()
	if f.validate_on_submit():
		a = Task(title=f.title.data, description = f.description.data, priority = f.priority.data )
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('getall'))
	
	return render_template('add.html', form=f, pageTitle='Form', data=data)

if __name__ == "__main__":
	app.run(debug=True)
