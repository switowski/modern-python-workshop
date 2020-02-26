"""URLs for our application."""

from flask import redirect, render_template, request
from todo import app
from todo.api import create_task, delete_task, finish_task, get_tasks


@app.route("/")
def tasks_list():
    """Main page of the application with the list of tasks."""
    tasks = get_tasks()
    # Render the HTML page located in "templates/application.html"
    # Passing tasks as a variable, so it can be used in the template
    return render_template("application.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def task_create():
    """Add a new Todo task."""
    body = request.form["body"]
    if not body:
        return "Error"
    # Save new Task in the database
    create_task(body)
    # Redirect user to the main page, so the new task will be displayed
    return redirect("/")


@app.route("/delete/<int:task_id>")
def task_delete(task_id):
    """Delete existing Todo task.

    :param task_id: ID of the task in the DB
    :type task_id: int
    """
    # Delete task from the database
    # NOTE: Usually you would check if the task was successfully deleted
    # (by catching an exception or checking the return status)
    # and render an error page if something went wrong
    delete_task(task_id)
    # Redirect user back to the main page, so the list of tasks will be updated
    return redirect("/")


@app.route("/done/<int:task_id>")
def task_done(task_id):
    """Mark Todo task as done.

    :param task_id: ID of the task in the DB
    :type task_id: int
    """
    # Mark task as done
    # NOTE: as in `task_delete` you might want to check for errors here
    finish_task(task_id)

    return redirect("/")
