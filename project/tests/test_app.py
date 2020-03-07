from todo.api import create_task, delete_task, finish_task, get_tasks


def test_list_tasks(test_app):
    # Make sure no tasks exist
    assert get_tasks() == []
    # Create some tasks
    create_task("buy milk")
    create_task("buy cookies")
    # Make sure we have 2 tasks now
    assert len(get_tasks()) == 2


def test_create_task(test_app):
    # Create a task
    create_task("Get milk")
    # Make sure it exists in the database
    existing_tasks = get_tasks()
    assert len(existing_tasks) == 1
    # Make sure the body of the task is correct
    first_task = existing_tasks[0]
    assert first_task.body == "Get milk"
    # Make sure the task is not done by default
    assert first_task.done is False


def test_delete_task(test_app):
    # Create a task and make sure it's stored in the DB
    create_task("Get milk")
    assert len(get_tasks()) == 1

    # Get the ID of the task (we need it to delete the task)
    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    # Delete the task
    delete_task(get_milk_id)

    # Make sure that there are no tasks
    assert len(get_tasks()) == 0



def test_finish_task(test_app):
    create_task("Get milk")
    assert len(get_tasks()) == 1

    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    finish_task(get_milk_id)

    get_milk = get_tasks().pop()
    assert get_milk.done is True
