"""Database models for our application."""

from todo import db


class Task(db.Model):
    """Database table to store Todo tasks."""

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """Better string representation of our task."""
        return f"<Task(id={self.id}, body={self.body})>"

