from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# This file initiates the application

app = Flask(__name__)
app.config['SECRET_KEY'] = '166f6e2c79cdca0cb597df5760a05b39'
# Setting up database (SQLITE database which is going to be a file on our filesystem)
# /// is relative path that is going to be created where app.py is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# what we pass here is the function name of the route
login_manager.login_view = 'login'
# its gonna stile the login message from login_view function
login_manager.login_message_category = 'info'

from final_project import routes