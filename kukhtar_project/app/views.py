from flask import Flask, render_template, url_for, request, flash, redirect, current_app
from app import app
import platform, sys
from datetime import datetime
from .forms import TaskForm, CategoryForm, LoginForm, RegistrationForm, UpdateAccountForm
from .models import Task, Category, User
from flask_sqlalchemy import SQLAlchemy
from app import db
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

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

@app.route('/task')
def getall():
	data = getData()
	args = Task.query.all()
	categories = []
	for i in args:
		categories.append(Category.query.get_or_404(i.category_id))
	return render_template('getall.html', args = args, len = len(args), data = data, categories = categories)

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

@app.route('/task/<int:id>/update', methods=['POST', 'GET'])
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
		return redirect(url_for('getall'))
	print('B')
	return render_template('update.html', form=f, pageTitle='Form', data=data, task=task_to_update)

@app.route('/task/create', methods=['POST', 'GET'])
def task():
	data = getData()
	f = TaskForm()
	f.categories.choices = get_categories_list()
	if f.validate_on_submit():
		a = Task(title=f.title.data, description = f.description.data, priority = f.priority.data, category_id = f.categories.data)
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('getall'))
	
	return render_template('add.html', form=f, pageTitle='Form', data=data)

def get_categories_list():
	args = Category.query.all()
	res = []
	for i in args:
		res.append((i.id, i.name))
	return res

@app.route('/category')
def getall_categories():
	data = getData()
	args = Category.query.all()
	return render_template('getall_categories.html', args = args, len = len(args), data = data)


@app.route('/category/create', methods=['POST', 'GET'])
def add_category():
	data = getData()
	f = CategoryForm()
	if f.validate_on_submit():
		a = Category(name=f.name.data)
		db.session.add(a)
		db.session.commit()
		return redirect(url_for('getall_categories'))
	
	return render_template('add-category.html', form=f, pageTitle='Form', data=data)

@app.route('/category/<int:id>')
def getCategory(id):
	data = getData()
	args = Category.query.get_or_404(id)
	return render_template('category.html', args = args, data = data)

@app.route('/category/<int:id>/delete')
def delete_category(id):
	task_to_delete = Category.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect(url_for('getall_categories'))
	except:
		return 'Can\'t delete category'

@app.route('/category/<int:id>/update', methods=['POST', 'GET'])
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
		return redirect(url_for('getall'))
	print('B')
	return render_template('update.html', form=f, pageTitle='Form', data=data, task=task_to_update)

@app.route('/register', methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	data = getData()
	f = RegistrationForm()
	print('AAAAAAAAAAAa')
	if f.validate_on_submit():
		print('AAAAAAAAAAAa')
		a = User(username=f.username.data, email = f.email.data, password = f.password.data)
		db.session.add(a)
		db.session.commit()
		print('AAAAAAAAAAAa')
		flash('Account created for ' + str(f.username.data), category = 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form=f, title='Register', data=data)

@app.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	data = getData()
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		print('asdasdasd')
		print(User.query.all())
		print('asdasdasd')

		record = User.query.filter_by(email=email).first() 
		print(record)
		if  record.password == password:
			login_user(record, remember=form.remember.data)
			flash('You have been loggin in!!!', category='success')
			return redirect(url_for('index'))
		else:
			flash('Login unsuccessful. Please check username and password', category = 'success')
	return render_template('login.html', form=form, title='Login', data=data)			
if __name__ == "__main__":
	app.run(debug=True)

@app.route("/logout")
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('index'))


@app.route("/account", methods=['POST', 'GET'])
@login_required
def account():
	form = UpdateAccountForm()
	user = db.session.query(User).filter_by(email=current_user.email).first()
	if form.validate_on_submit():
		# if form.picture.data:
		# 	picture_file = form.picture.data
		# 	user.image_file = picture_file
		f = form.picture.data
		f.save(secure_filename(f.filename))
		user.username = form.username.data
		user.email = form.email.data
		user.image_file = f.filename
		db.session.commit()
		print(user.username)
		flash('Your account has been updated !', 'success')
		return redirect(url_for('index'))
	elif request.method == 'GET':
		print(user.username)
		form.username.data = user.username 
		form.email.data = user.email
	# image_file = url_for('static', form=form)
	data = getData()
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', data=data, form=form, image_file=image_file)


# def save_picture(form_pictute):
# 	random_hex = secrets.token_hex(8)
# 	_, f_ext = os.path.splitext(form_pictute.filename)
# 	picture_fn = random_hex + f_ext
# 	picture_path = os.path.join(
# 		current_app.root_path, 'static/img/profile_pics', picture_fn)

# 	img = Image.open(form_pictute)
# 	img_w, img_h = img.size
# 	if img_w < 500 or img_h < 500:
# 		if img_w > img_h:
# 			output_size = (img_h, img_h)
# 			img = ImageOps.fit(img, output_size, Image.ANTIALIAS)
# 		else:
# 			output_size = (img_w, img_w)
# 			img = ImageOps.fit(img, output_size, Image.ANTIALIAS)
# 	else:
# 		output_size = (500, 500)
# 		img = ImageOps.fit(img, output_size, Image.ANTIALIAS)

# 	img.save(picture_path)

# 	return picture_fn