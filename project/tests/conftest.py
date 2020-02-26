import pytest
from flask import Flask
from todo import db as _db


@pytest.fixture
def test_app():
    """Set up test Flask application."""

    # Set up Flask app
    app = Flask(__name__)
    # We will create database in memory
    # That way, we don't worry about after cleaning/removing it after running tests
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    _db.init_app(app)

    with app.app_context():
        # Create database tables
        _db.create_all()
        yield app
        # Our database is stored in memory so the following line is not needed
        # I'm using it to show you how to clean up after your tests
        _db.drop_all()
