from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '166f6e2c79cdca0cb597df5760a05b39'
# Setting up database (SQLITE database which is going to be a file on our filesystem)
# /// is relative path that is going to be created where app.py is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from final_project import routes