from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import (DataRequired,
                        Regexp,
                        ValidationError,
                        Email,
                        EqualTo,
                        Length)


from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("User with that name already exists.")


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("User with that email already exists.")


class RegisterForm(Form):
    email = StringField(
            'Email',
            validators=[
                DataRequired(),  # there must be data
                Email(),
                email_exists
            ])
    password = PasswordField(
            'Password',
            validators=[
                DataRequired(),
                Length(min=2),
                EqualTo('password2', message='Passwords must match')
            ])
    password2 = PasswordField(
            'Confirm Password',
            validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class TacoForm(Form):
    protein = StringField('Protein')
    cheese = BooleanField('Cheese')
    shell = StringField('Shell')
    extras = StringField('Extras')