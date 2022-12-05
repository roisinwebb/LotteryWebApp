from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import re


def validate_data(data_field):
    p = re.compile("regex goes here")
    if not p.match(data_field.data):
        raise ValidationError("error message goes here")


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[Length(min=6, max=12)])
    confirm_password = PasswordField(validators=[EqualTo('password', message='Both password fields must be equal!')])
    submit = SubmitField(validators=[DataRequired()])

 myString = StringField(validators=[])

r'(?=.*\d)(?=.*[a-zA-Z])(?=.*[+*.${}]'