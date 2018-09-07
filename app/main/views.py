# from flask_login import login_required
# from flask import render_template,redirect,url_for, flash,request
# from flask_login import login_user
# from ..models import User
# from .forms import LoginForm,RegistrationForm
# from .. import db
from .import main

@main.route('/home')
def index():

     return render_template('home.html')

