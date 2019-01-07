from flask_wtf import FlaskForm
# wtforms is part of FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from final_project.models import User

class RegistrationForm(FlaskForm):
    # validators are classes used to make sure 'username' has certain limitations for better
    # user experience 
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Validation of username field (check if username is already in db)
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please Choose a different one.')
    
    # Validation of email field (check if username with that email is already in db)
    def validate_email(self, email):
        # user with that email
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken.')

class LoginForm(FlaskForm):
    # validators are classes used to make sure 'username' has certain limitations for better
    # user experience 
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    # this is a secure coockie that makes sure user is remembered on site after login
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
