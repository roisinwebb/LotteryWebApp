from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf import RecaptchaField
import re


# FORMS
# characters to be excluded in first name and last name
def character_check(form, field):
    excluded_chars = "* ? ! ' ^ + % & / ( ) = } ] [ { $ # @ < >"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")


# password must contain at least 1 uppercase, 1 lowercase, 1 digit and 1 special character
def validate_data(form, password):
    p = re.compile(r'(?=.*\d)(?=.*[a-zA-Z])(?=.*\W)')
    if not p.match(password.data):
        raise ValidationError("Must contain at least 1 digit, 1 lowercase, 1 uppercase and a special character ")


# phone number must be in the format XXXX-XXX-XXXX
def validate_number(form, phone):
    p = re.compile(r'(\d{4})-(\d{3})-(\d{4})')
    if not p.match(phone.data):
        raise ValidationError("Must be in the format XXXX-XXX-XXXX")


# registration form for website
class RegisterForm(FlaskForm):
    # email format is needed and data must be added
    email = EmailField(validators=[DataRequired(), Email()])
    # data must be added and character check for no special characters
    firstname = StringField(validators=[DataRequired(), character_check])
    # data must be added and character check for no special characters
    lastname = StringField(validators=[DataRequired(), character_check])
    # data must be added and phone number format
    phone = StringField(validators=[DataRequired()])
    # password must be added and must be between 6 and 12 characters
    password = PasswordField(validators=[DataRequired(), validate_data, Length(min=6, max=12)])
    # password must be added and both passwords must match
    confirm_password = PasswordField(validators=[DataRequired(), validate_data, EqualTo('password',
                                                                    message='Both password ' 'fields must be equal!')])
    submit = SubmitField()


# login form for website
class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    recaptcha = RecaptchaField()
    pin = StringField(validators=[DataRequired()])
    submit = SubmitField()
