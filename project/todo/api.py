"""API functions to interact with TODO tasks."""

from todo.models import Task, db


def get_tasks():
    """Return all the existing tasks.

    :return: List of tasks
    :rtype: list
    """
    return Task.query.all()


def create_task(body):
    """Create a new task in the DB.

    :param body: Text of a Todo task
    :type body: str
    """
    task = Task(body=body)
    db.session.add(task)
    db.session.commit()


def delete_task(task_id):
    """Delete existing task.

    :param task_id: ID of the task to delete
    :type task_id: int
    """
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()


def finish_task(task_id):
    """Mark task as done.

    :param task_id: ID of the task to finish
    :type task_id: int
    """
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()
