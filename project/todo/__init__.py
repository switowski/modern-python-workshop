"""By creating this file, we turn "todo" directory into a Python package.

Usually the __init__.py file is empty.
One of the reasons why you might put some code here is convenience.
All the functions and variables from this file can be imported with just:
from todo import app, db
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Set up Flask and sqlite database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
# The following line is needed to suppress SQLALCHEMY_TRACK_MODIFICATIONS warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# This import has to be AFTER the "app" and "db" setup!
# Otherwise you will run into circular imports issues
# Here is another idea how to deal with them:
# https://stackoverflow.com/a/42910185
from todo import views  # noqa E402 isort:skip

