=====================
 django-evil-project
=====================

Installation
============

I recommend to use `pyenv <https://github.com/yyuu/pyenv>`_ to manage you virtual environments, but you can do something like this with virtualenv[wrapper] or just install python packages globally.

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

Bower dependencies
------------------

Also you must install Bower dependencies:

.. code-block:: bash

   $ bower i

Local settings
--------------

Create a ``config/settings/local.py`` file (it's ignored by git) with local settings or remove this import from ``config/settings/__init__.py``. Minimal ``local.py`` file can contain this code:

.. code-block:: python

   from .development import *  # noqa
