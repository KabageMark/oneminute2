from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from ..models import User,Pitch,Comment
from .forms import pitchForm,LoginForm,RegistrationForm,commentForm
from .. import db
from .import main

@main.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password_hash  = form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
        title = "New Account"
    return render_template('register.html',form = form)


@main.route("/home/pitch",methods=['GET','POST'])
def pitching():

    form=pitchForm()
    if form.validate_on_submit():
        pitch=Pitch(pitch=form.pitch.data,category=form.category.data)
        pitch.save_pitch()
        return redirect(url_for('main.postedpitch'))
    return render_template('pitch.html',form=form)


  
@main.route("/home/",methods=['GET','POST'])
def postedpitch():
    Comment_form=commentForm()
    comment = Comment.query.filter_by(comment='').all()
    username = Comment.query.filter_by(username='').all()
    
    business = Pitch.query.filter_by(category='business').all()
    love = Pitch.query.filter_by(category='love').all()
    investment = Pitch.query.filter_by(category='investment').all()
    science = Pitch.query.filter_by(category='science').all()

    return render_template('posted.html',business=business,love=love,investment=investment,science=science,Comment_form=Comment_form,comment=comment,username=username)









@main.route('/',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.pitching'))

        flash('Invalid username or Password')

    title = "pitch login"
    return render_template('index.html',form = login_form,title=title)





@main.route('/logout')
@login_required
def logout():
    logout_user()

    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))    



 