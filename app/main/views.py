# from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request
# from flask_login import login_user
# from ..models import User
from .forms import LoginForm,RegistrationForm
# from .. import db
from .import main

# @main.route('/home')
# def index():

#      return render_template('home.html')

@main.route("/home",methods=['GET','POST'])
def home():
    form = pitchForm()    
    pitch = form.pitch.data
    category = form.category.data
    comments = form.comments.data
    print(pitch)
    print(category)
    print(comments) 
    return render_template('home.html',pitch=pitch, category=category,comments=comments,form = form)
