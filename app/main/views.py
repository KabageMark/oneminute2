from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from ..models import User
from .forms import pitchForm,LoginForm,RegistrationForm
from .. import db
from .import main

  
@main.route("/home/",methods=['GET','POST'])
def home():
    form = pitchForm()
    pitch = form.pitch.data
    category = form.category.data
    comments = form.comments.data
    print(pitch)
    print(category)
    print(comments) 
    return render_template('home.html',pitch = pitch, category = category,comments = comments,form = form)




@main.route('/',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "pitch login"
    return render_template('index.html',form = login_form,title=title)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))    


@main.route('/home/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data,confirm_password = form.password_confirm.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
        title = "New Account"
    return render_template('register.html',form = form)
