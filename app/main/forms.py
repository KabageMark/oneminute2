from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField,BooleanField,RadioField,TextAreaField
from wtforms.validators import DataRequired,Required, Length , Email , EqualTo
from ..models import User,Pitch

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



class pitchForm(FlaskForm):
    pitch = StringField('Pitch',validators=[DataRequired()])

    category = RadioField('Category',choices=[("business","business"),("love","love"),("investment" ,"investment"),("science","science")],validators=[DataRequired()])

    submit = SubmitField('submit')

class commentForm(FlaskForm):
    comment = StringField('Comment')

    username = StringField('Username')

    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')