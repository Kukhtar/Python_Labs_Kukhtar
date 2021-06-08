from flask import Flask, render_template, url_for, request, flash, redirect, current_app, Blueprint
import platform, sys
from datetime import datetime
from .forms import TaskForm, CategoryForm, LoginForm, RegistrationForm, UpdateAccountForm
from models import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from extensions.database import db

login_bp = Blueprint('login_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='')

def getData():
	now = datetime.now()
	return ["User: " + str(request.headers.get('User-Agent')) , "Platform: " + str(platform.system()) + "Python version:" + str(sys.version_info[0]) + "   Time: " + str(now.strftime("%H:%M:%S"))]

@login_bp.route('/')
def log_index():
	data = getData()
	return render_template('log_index.html', data = data)

@login_bp.route('/register', methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('login_bp.log_index'))
	data = getData()
	f = RegistrationForm()
	if f.validate_on_submit():
		a = User(username=f.username.data, email = f.email.data, password = f.password.data)
		db.session.add(a)
		db.session.commit()
		flash('Account created for ' + str(f.username.data), category = 'success')
		return redirect(url_for('login_bp.login'))
	return render_template('register.html', form=f, title='Register', data=data)

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('login_bp.log_index'))
	data = getData()
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data
		print(User.query.all())

		record = User.query.filter_by(email=email).first() 
		print(record)
		if  record.password == password:
			login_user(record, remember=form.remember.data)
			flash('You have been loggin in!!!', category='success')
			return redirect(url_for('login_bp.log_index'))
		else:
			flash('Login unsuccessful. Please check username and password', category = 'success')
	return render_template('login.html', form=form, title='Login', data=data)			
if __name__ == "__main__":
	app.run(debug=True)

@login_bp.route("/logout")
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('login_bp.log_index'))


@login_bp.route("/account", methods=['POST', 'GET'])
@login_required
def account():
	form = UpdateAccountForm()
	user = db.session.query(User).filter_by(email=current_user.email).first()
	if form.validate_on_submit():
		# if form.picture.data:
		# 	picture_file = form.picture.data
		# 	user.image_file = picture_file
		f = form.picture.data
		f.save("static/profile_pics/" + f.filename)
		user.username = form.username.data
		user.email = form.email.data
		user.image_file = f.filename
		db.session.commit()
		print(user.username)
		flash('Your account has been updated !', 'success')
		return redirect(url_for('login_bp.log_index'))
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