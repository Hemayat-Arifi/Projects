from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import datetime
from pytube import YouTube
import sys
import os



app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisishemotubesecretkey'
migrate = Migrate(app, db)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(85), nullable=False)
    posts = db.relationship('Posts', backref='poster')
  

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))




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



class PostForm(FlaskForm):
    name = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Video Name"})

    creator = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Your Username"})

    desc = StringField(validators=[
                             InputRequired(), Length(min=5, max=150)], render_kw={"placeholder": "Description"})

    date = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Date"})

    submit = SubmitField('Submit')



# __________________________________________ Functions _________________________________________

def download_video_highest(link):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    print("Success !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def download_video_lowest(link):
    yt = YouTube(link)
    video = yt.streams.get_lowest_resolution()
    print("Success !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")       

def download_video_audio(link):
    yt = YouTube(link)
    video = yt.streams.get_audio_only()
    print("Success !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# __________________________________________ Routes  __________________________________________

@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        a = request.form["url"]    

    return render_template("index.html")



@app.route("/download", methods=["POST", "GET"])
def download():
    url = request.form["url"]
    resolution = request.form["resolution"]

    if resolution == "1":
        download_video_highest(url)
        print(url)
        print(resolution)
    
    elif resolution == "2":
        download_video_lowest(url)
        print(url)
        print(resolution)
    
    elif resolution == "3":
        download_video_audio(url)
        print(url)
        print(resolution)

    else:
        print("Sorry")
        print(url)
        print(resolution)

    return render_template("download.html")



@app.route("/login", methods=["POST", "GET"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('profile'))
            else:
                pass
                 
        else:
            flash("Wrong Credentials!")
    else:
        pass

    return render_template("login.html", form=form)



@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form=form)



@app.route("/profile", methods=["POST", "GET"])
@login_required
def profile():

    return render_template("profile.html")



@app.route("/profile/create", methods=["POST", "GET"])
@login_required
def create():
    form = PostForm()
    x = datetime.datetime.now()

    if form.validate_on_submit():
        poster = current_user.username
        new_post = Posts(name=form.name.data, desc=form.desc.data, creator=poster)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('profile'))

    return render_template("create.html", form=form, date=x)



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()

    return redirect(url_for('login'))



if __name__ == "__main__":
    app.debug = True
    app.run()

