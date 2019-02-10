# for environment variables
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# This file initiates the application
# app is an instance of a Flask class
app = Flask(__name__)

''' Configuration for app '''
# config is a subclass
app.config['SECRET_KEY'] = '166f6e2c79cdca0cb597df5760a05b39'
# Setting up database (SQLITE database) which is going to be a file on our filesystem)
# /// is relative path that is going to be created where 'app' is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#db is a SQLAlchemy object in which the application 'app' is passed
db = SQLAlchemy(app)

# class wrapper in which Flask app object is wrapped
bcrypt = Bcrypt(app)

# The login manager contains the code that lets application and Flask-Login work together
# By default, Flask-Login uses sessions for authentication
login_manager = LoginManager(app)
# By default, when a user attempts to access a login_required view without being logged in, 
# Flask-Login will flash a message and redirect them to the log in view
# what we pass here is the function name of the route (log in view)
login_manager.login_view = 'login'
# its gonna style the login message from login_view function
login_manager.login_message = u'You have to be logged in to access this page!'
login_manager.login_message_category = 'info'

''' Configuration for mail server '''
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# USER and PASSWORD are used just as an example 
app.config['MAIL_USERNAME'] = os.environ.get('USER')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')

# all emails are sent using the configuration values of
# the application that was passed to the Mail class constructor.
mail = Mail(app)


from final_project import routes

