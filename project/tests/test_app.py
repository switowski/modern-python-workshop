import pytest
from todo.api import get_tasks


@pytest.mark.xfail(reason="This test fails because we don't have create_task function")
def test_list_tasks(test_app):
    # Make sure no tasks exist
    assert get_tasks() == []
    # Create some tasks
    create_task("buy milk")
    create_task("buy cookies")
    # Make sure we have 2 tasks now
    assert len(get_tasks()) == 2


# TODO: Write tests to create/delete/finish a task
