Django-yarnpkg
==============

Easy way to use `yarnpkg <http://yarnpkg.com/>`_ with your `Django <https://www.djangoproject.com/>`_ project.

This is a fork of `django-bower <https://github.com/nvbn/django-bower>` by Vladimir Iakovlev.

Read full documentation on `read-the-docs <https://django-yarnpkg.readthedocs.io/en/latest/>`_.

Installation
------------

Install django-yarnpkg package:

.. code-block:: bash

    pip install django-yarnpkg

Add django-bower to `INSTALLED_APPS` in your settings:

.. code-block:: python

    'django_yarnpkg',

Add staticfinder to `STATICFILES_FINDERS`:

.. code-block:: python

    'django_yarnpkg.finders.NodeModulesFinder',

Specify path to components root (you need to use an absolute path):

.. code-block:: python

    NODE_MODULES_ROOT = os.path.join(BASE_DIR, 'node_modules')


If you need, you can manually set the path to yarnpkg:

.. code-block:: python

    YARN_PATH = '/usr/bin/yarnpkg'

You can see an example settings file in `example project <https://edugit.org/nik/django-yarnpkg/blob/master/example/example/settings.py>`_.

Usage
-----

Specify `YARN_INSTALLED_APPS` in settings, like:

.. code-block:: python

    YARN_INSTALLED_APPS = (
        'bootstrap@^4.4.1',
        'underscore@^1.6.1',
    )

Download yarn packages with the management command:

.. code-block:: bash

    ./manage.py yarn install

Add scripts in the template, like:

.. code-block:: html+django

    {% load static %}
    <script type="text/javascript" src='{% static 'jquery/dist/jquery.js' %}'></script>

In production you need to call `yarnpkg install` before `collectstatic`:

.. code-block:: bash

    ./manage.py yarn install
    ./manage.py collectstatic

If you need to pass arguments to yarnpkg, like `--flat`, use:

.. code-block:: bash

    ./manage.py yarn install -- --flat

You can call yarnpkg commands like `info` and `update` with:

.. code-block:: bash

    ./manage.py yarn info backbone
    ./manage.py yarn update

Python 3 support
----------------
django-yarnpkg supports python 3.3+
