TODO Application
================

This is a simple TODO application.

Setup
-----

Create virtual environment:

.. code-block:: shell

    $ python -m venv venv

Activate it:

.. code-block:: shell

    $ source venv/bin/activate

Install required packages:

.. code-block:: shell

    $ pip install -r requirements.txt

Start server

.. code-block:: shell

    # Enable development mode for auto reloading and verbose errors
    $ export FLASK_ENV=development
    $ python run.py

If everything worked fine, you should be able to navigate to: http://127.0.0.1:5000 in your browser and see the TODO application.

Application structure
---------------------

This application consists of the following parts:

* ``run.py`` - main file of the application. When run with Python, starts the web server.
* ``requirements.txt`` - list of Python packages used by the application.
* ``todo/__init__.py`` - turns ``todo`` directory into a Python package, but also exports the ``app`` and ``db`` objects so they can  be used in the ``run.py`` function.
* ``todo/api.py`` - contains the API of the application - all the functions to create/list/delete/finish the TODO tasks.
* ``todo/models.py`` - database models for the application.
* ``todo/views.py`` - connects the URLs that users will visit with the API functions.
* ``tests/conftest.py`` - contains a fixture to create a test application.
* ``tests/test_app.py`` - tests for the application.
* ``docs`` - documentation for the application. Run ``$ ./docs/make build html`` command and open the ``docs/build/html/index.html`` file in the browser to read it.


Basic functionality
-------------------

This application should implement the following features:

* Show a list of tasks on the main page of the application and a form to add a new task
* When a user adds a new task, the page should be reloaded to display the updated list
* User can mark task as "Done" (those tasks should be displayed differently from others)
* User can delete a task (without marking it as done)

Don't forget to:
* Add some tests in the ``tests`` directory
* Document your functions and generate the documentation with Sphinx


Further improvements
--------------------

If you want to add more features to this simple app, you can:

* Add function to mark finished tasks as "unfinished" (and change the "Done" button into "Undo" based on the current state of the task).
* Stop deleting the database each time we restart the application (or even use a more "production-grade" database like PostgreSQL)
* Add categories to our tasks (and display them in the frontend grouped by those categories)
* Test if the views are working fine - but to make it work, you need to decouple the code a bit by using Flask blueprints (check out the ``test-views-with-blueprints`` branch of this repository to see how to make it work).
* Dockerize it
