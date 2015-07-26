=====================
 django-evil-project
=====================

A project template for Django 1.8.

Features
========

- For Django 1.8
- Per-environment settings (development, testing, production)
- Preinstalled packages:

  - `psycopg2 <https://pypi.python.org/pypi/psycopg2>`_
  - `django-braces <https://github.com/brack3t/django-braces>`_
  - `django-model-utils <https://github.com/carljm/django-model-utils>`_
  - Development only:

    - `django-extensions <https://github.com/django-extensions/django-extensions>`_
    - `django-debug-toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_
    - `bpython <http://bpython-interpreter.org/screenshots>`_
    - `django-template-debug <https://github.com/calebsmith/django-template-debug>`_

  - Test only:

    - `django-rainbowtests <https://github.com/bradmontgomery/django-rainbowtests>`_
    - `coverage <https://pypi.python.org/pypi/coverage/3.7.1>`_

  - Production only:

    - `gunicorn <http://gunicorn.org/>`_
- `Browserify <http://browserify.org/>`_ support
- `PostCSS <https://github.com/postcss/postcss>`_ support with `autoprefixer <https://github.com/postcss/autoprefixer>`_ integration

Installation
============

We recommend to use `pyenv <https://github.com/yyuu/pyenv>`_ to manage you virtual environments, but you can do something like this with virtualenv[wrapper] or just install python packages globally.

First of all you need a fresh copy of Django framework.

.. code-block:: bash

   $ pyenv virtualenv example
   $ pip install django

Then you can create a new Django project with django-evil-project template:

.. code-block:: bash

   $ django-admin startproject --template https://github.com/ssbb/django-evil-project/zipball/master myproject

Installation of dependencies
----------------------------

Depending on where you are installing dependencies:

For development (including packages for testing):

.. code-block:: bash

   $ pip install -r requirements/development.txt

For production:

.. code-block:: bash

   $ pip install -r requirements/production.txt

Node.js dependencies
--------------------

If you need Browserify and PostCSS support, you must have node.js installed and then install required dependencies:

.. code-block:: bash

   $ npm i

npm run commands
================

build
-----

Build js and css files with ``build-stylesheets`` and ``build-javascripts`` commands.

watch
-----

Watch for changes in js and css files, re-compile it and reload browser with livereload.

build-stylesheets
-----------------

Builds ``staticfiles/stylesheets/app.css`` stylesheet into ``staticfiles/build`` directory with PostCSS.

build-javascripts
-----------------

Builds ``staticfiles/javascripts/app.js`` script into ``staticfiles/build`` directory with Browserify.

watch-stylesheets
-----------------

Watching for changes in stylesheets and re-compiles it with PostCSS.

watch-javascripts
-----------------

Watching for changes in javascript files and re-compiles it with Watchify.

livereload
----------

Watchinf for changes in ``staticfiles`` directory and reloading changes in browser.
