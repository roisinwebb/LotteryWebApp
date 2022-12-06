from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import re

def character_check(form, field):
    excluded_chars = "!£$%^&*()-+@~#?"
    for char in field.data:
        if char in excluded_chars:
      raise ValidationError(f"Character{char} is not allowed.")

 def validate_data(form, password):
    p = re.compiler(r'(?=.*\d)(?=.*[a-zA-Z])(?=.*[+!"£$%^&*()-=[{]};:@#~/?.>,<\|])')
    if p.match(password.data):
        return
    raise ValidationError("Must contain at least 1 digit, contain at least 1 lowercase, 1 upper case character  and at least 1 special character")

class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[Length(min=6, max=12), character_check(), DataRequired()])
    confirm_password = PasswordField(validators=[EqualTo('password', message='Both password fields must be equal!'), character_check(), DataRequired()])
    submit = SubmitField(validators=[DataRequired()])



