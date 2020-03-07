"""By creating this file, we turn "todo" directory into a Python package.

Usually the __init__.py file is empty.
One of the reasons why you might put some code here is convenience.
All the functions and variables from this file can be imported with just:
from todo import app, db
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from todo.models import db
from todo.views import simple_page

# Set up Flask and sqlite database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
# The following line is needed to suppress SQLALCHEMY_TRACK_MODIFICATIONS warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.register_blueprint(simple_page)
db.init_app(app)
