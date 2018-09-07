from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField,BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo





class pitchForm(FlaskForm):
    pitch = StringField('Pitch',validators=[DataRequired()])

    category = StringField('Category',validators=[DataRequired()])

    comments = StringField('Comments')

    submit = SubmitField('submit') 