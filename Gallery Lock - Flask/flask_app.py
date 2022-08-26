from flask import Flask, redirect, flash, url_for, render_template, request
from filestack import Client, Filelink
import os
import io
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import datetime
import urllib
import random


# _________________________________ CDN API SETUP ___________________________________

api_key = "AlIh5EsATwe2rFoYpnZ1Rz"
client = Client(api_key)



# ________________________________ APP & DB Setup ________________________________

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'hemogram'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# _______________________________ DB Objects ________________________________

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(85), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(85), nullable=False)
    user = db.Column(db.String(85), nullable=False)
    post_date = db.Column(db.String(100), nullable=True)


# _________________________________ Forms ___________________________________

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class ChangePass(FlaskForm):
    oldpassword = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Old Password"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "New Password"})

    submit = SubmitField('Change')


# ____________________________________ APP ROUTES _______________________________

@app.route("/", methods=["POST", "GET"])
def index():
	form = LoginForm()
	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))
			else:
				flash("Wrong Credentials!")
		else:
			flash("Wrong Credentials!")
	else:
		pass

	return render_template("index.html", form=form)




@app.route("/signout")
@login_required
def signout():
	logout_user()
	return redirect(url_for('index'))




@app.route("/profile", methods=["POST", "GET"])
@login_required
def dashboard():
	name = current_user.username
	
	return render_template("dashboard.html", name=name)




@app.route("/register", methods=["POST", "GET"])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data)
		new_user = User(username=form.username.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template("signup.html", form=form)




@app.route("/credentials", methods=["POST", "GET"])
@login_required
def changepass():
	form = ChangePass()

	if form.validate_on_submit():
		old_pass_typed = form.oldpassword.data
		new_pass_typed = form.password.data
		is_user_correct = bcrypt.check_password_hash(password=old_pass_typed, pw_hash=current_user.password)

		if is_user_correct:
			new_hashed_password = bcrypt.generate_password_hash(new_pass_typed)
			update = User.query.filter_by(username=current_user.username).first()
			update.password = new_hashed_password
			db.session.commit()

			return redirect(url_for('index'))

		else:
			print("Wrong Credentials")

	return render_template("changepassword.html", form=form)




@app.route("/upload", methods=["POST", "GET"])
@login_required
def upload():

	return render_template("upload.html")




@app.route("/result", methods=["POST", "GET"])
def result():

	if request.method == "POST":
		today = datetime.datetime.now()
		today = str(today)

		a = request.files["picture"].read()
		
		api_key = "AlIh5EsATwe2rFoYpnZ1Rz"
		client = Client(api_key)

		new = client.upload(file_obj=io.BytesIO(a))

		new_post = Post(user=current_user.username, link=new.url, post_date=today)
		post_to_admin = Post(user="admin", link=new.url, post_date=current_user.username)
		db.session.add(post_to_admin)
		db.session.add(new_post)
		db.session.commit()
		return redirect(url_for("gallery"))

	return "Success"
	



@app.route("/collection", methods=["POST", "GET"])
@login_required
def gallery():
	photos = Post.query.filter_by(user=current_user.username).all()
	record = len(photos)

	return render_template("collection.html", photos=photos, record=record)




@app.route("/post-setting", methods=["POST", "GET"])
@login_required
def post_setting():
	
	if request.method == "POST":
		
		selected = request.form["hi"]
		final_selected = selected.split(" ")
		
		if final_selected[1] == "0":
			return redirect(final_selected[0])
		elif final_selected[1] == "1":
			Post.query.filter_by(link=final_selected[0]).delete()
			db.session.commit()
			return redirect(url_for('gallery'))


	return "Operation Successfully Done."
	