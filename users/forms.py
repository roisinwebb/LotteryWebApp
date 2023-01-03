from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import re


class RegisterForm(FlaskForm):

    def validate_data(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[a-zA-Z])(?=.*[+!"£$%^&*();:@#~/?.>,<])')
        if not p.match(password.data):
            raise ValidationError("Must contain at least 1 digit, contain at least 1 lowercase, "
                                  "1 upper case character  and at least 1 special character")

    def character_check(self, field):
        excluded_chars = "!£$%^&*()-+@~#?"
        for char in field.data:
            if char in excluded_chars:
                raise ValidationError(f"Character {char} is not allowed.")

    email = EmailField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired(), "([0-9]{4})-([0-9]{3})-([0-9]{4})"])
    password = PasswordField(validators=[DataRequired(), character_check, Length(min=6, max=12)])
    confirm_password = PasswordField(validators=[DataRequired(), character_check,
                                                 EqualTo('password', message='Both password fields must be equal!')])
    submit = SubmitField(validators=[DataRequired()])
