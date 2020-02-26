"""Main file of our application.

When ran with:
$ python run.py
it will reset the database and start the webserver.
"""

from todo import app, db


if __name__ == "__main__":

    db.drop_all()
    db.create_all()

    app.run()
