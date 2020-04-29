from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=14)])
    username = StringField("Username", [validators.Length(min=1, max=14)])
    password = PasswordField("Password", [validators.Length(min=8, max=30), validators.EqualTo('confirmPassword', message='Passwords must match')])
    confirmPassword = PasswordField("Confirm password")

    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()

        if user:
            raise ValidationError('That name is already taken. Please choose another one.')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is already taken. Please choose another one.')

    
    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    newPassword = PasswordField('New password', [validators.Length(min=8, max=30), validators.EqualTo('newPasswordConfirm', message='Passwords must match')])
    newPasswordConfirm = PasswordField('Confirm your new password')

    class Meta:
        csrf = False
