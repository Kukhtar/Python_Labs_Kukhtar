from flask import Flask, render_template, url_for, request, flash, redirect, Blueprint
from models import Task, Category
from flask_sqlalchemy import SQLAlchemy
from extensions.database import db
from datetime import datetime
import platform, sys
from .forms import TaskForm, CategoryForm


tasks_bp = Blueprint('tasks_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='')

def getData():
	now = datetime.now()
	return ["User: " + str(request.headers.get('User-Agent')) , "Platform: " + str(platform.system()) + "Python version:" + str(sys.version_info[0]) + "   Time: " + str(now.strftime("%H:%M:%S"))]

@tasks_bp.route('/task_bp')
def task_bp():
	data = getData()
	return render_template('task_bp.html', data = data)

@tasks_bp.route('/task')
def getall():
	data = getData()
	args = Task.query.all()
	categories = []
	for i in args:
		categories.append(Category.query.get_or_404(i.category_id))
	return render_template('getall.html', args = args, len = len(args), data = data, categories = categories)

@tasks_bp.route('/task/<int:id>')
def getTask(id):
	data = getData()
	args = Task.query.get_or_404(id)
	return render_template('task.html', args = args, data = data)

@tasks_bp.route('/task/<int:id>/delete')
def delete(id):
	task_to_delete = Task.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect(url_for('tasks_bp.getall'))
	except:
		return 'Can\'t delete task'

@tasks_bp.route('/task/<int:id>/update', methods=['POST', 'GET'])
def update(id):
	task_to_update = Task.query.get_or_404(id)
	data = getData()
	f = TaskForm()
	# f.populate_obj(task_to_update)
	if request.method == 'POST':
		print('A')
		task_to_update.title = f.title.data
		task_to_update.description = f.description.data
		task_to_update.priority = f.priority.data
		
		db.session.commit()
		return redirect(url_for('tasks_bp.getall'))
	print('B')
	return render_template('update.html', form=f, pageTitle='Form', data=data, task=task_to_update)

@tasks_bp.route('/task/create', methods=['POST', 'GET'])
def task():
	data = getData()
	f = TaskForm()
	f.categories.choices = get_categories_list()
	if f.validate_on_submit():
		a = Task(title=f.title.data, description = f.description.data, priority = f.priority.data, category_id = f.categories.data)
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('tasks_bp.getall'))
	
	return render_template('add.html', form=f, pageTitle='Form', data=data)

def get_categories_list():
	args = Category.query.all()
	res = []
	for i in args:
		res.append((i.id, i.name))
	return res

@tasks_bp.route('/category')
def getall_categories():
	data = getData()
	args = Category.query.all()
	return render_template('getall_categories.html', args = args, len = len(args), data = data)


@tasks_bp.route('/category/create', methods=['POST', 'GET'])
def add_category():
	data = getData()
	f = CategoryForm()
	if f.validate_on_submit():
		a = Category(name=f.name.data)
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('tasks_bp.getall_categories'))
	
	return render_template('add-category.html', form=f, pageTitle='Form', data=data)

@tasks_bp.route('/category/<int:id>')
def getCategory(id):
	data = getData()
	args = Category.query.get_or_404(id)
	return render_template('category.html', args = args, data = data)

@tasks_bp.route('/category/<int:id>/delete')
def delete_category(id):
	task_to_delete = Category.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect(url_for('tasks_bp.getall_categories'))
	except:
		return 'Can\'t delete category'

@tasks_bp.route('/category/<int:id>/update', methods=['POST', 'GET'])
def update_category(id):
	task_to_update = Task.query.get_or_404(id)
	data = getData()
	f = TaskForm()
	# f.populate_obj(task_to_update)
	if request.method == 'POST':
		print('A')
		task_to_update.title = f.title.data
		task_to_update.description = f.description.data
		task_to_update.priority = f.priority.data
		
		db.session.commit()
		return redirect(url_for('tasks_bp.getall'))
	print('B')
	return render_template('update.html', form=f, pageTitle='Form', data=data, task=task_to_update)

