Cookbook
========

Calling a Django management command
-----------------------------------

.. versionadded:: 0.9

If you want to call a Django management command programmatically, say
from a script outside of your usual Django code, you can use the
equivalent of Django's :func:`~django.core.management.call_command`
function with django-configurator, too.

Simply import it from ``dj_configurator.management`` instead:

.. code-block:: python
   :emphasize-lines: 1

    from dj_configurator.management import call_command

    call_command('dumpdata', exclude=['contenttypes', 'auth'])

Read .env file
--------------

Configurations can read values for environment variables out of an ``.env``
file, and push them into the application's process environment. Simply set
the ``DOTENV`` setting to the appropriate file name:

.. code-block:: python

   # mysite/settings.py

   import os.path
   from dj_configurator import Configuration, values

   BASE_DIR = os.path.dirname(os.path.dirname(__file__))

   class Dev(Configuration):
       DOTENV = os.path.join(BASE_DIR, '.env')

       SECRET_KEY = values.SecretValue()
       API_KEY1 = values.Value()
       API_KEY2 = values.Value()
       API_KEY3 = values.Value('91011')
       

A ``.env`` file is a ``.ini``-style file. It must contain a list of
``KEY=value`` pairs, just like Shell environment variables:

.. code-block:: ini

   # .env

   DJANGO_DEBUG=False
   DJANGO_SECRET_KEY=1q2w3e4r5t6z7u8i9o0(%&)$§!pqaycz
   API_KEY1=1234
   API_KEY2=5678

``DOTENV`` can also be a dictionary, and then its behavior can be configured more:
.. code-block:: python
   BASE_DIR = os.path.dirname(os.path.dirname(__file__))

   class Dev(Configuration):
       DOTENV = {
            "path": str(os.path.join(BASE_DIR, '.env')),
            # if True, overrides previously set environmental variables, if False only sets them if they haven't been set before 
            "override": True,
            # if True errors if the DOTENV is not found at path, if False return
            "required": False,
            # if True, reloads DOTENV dynamically for example on hot reload
            "reload": True,

Envdir
------

envdir_ is an effective way to set a large number of environment variables
at once during startup of a command. This is great in combination with
django-configuration's :class:`~dj_configurator.values.Value` subclasses
when enabling their ability to check environment variables for override
values.

Imagine for example you want to set a few environment variables, all you
have to do is to create a directory with files that have capitalized names
and contain the values you want to set.

Example:

.. code-block:: console

    $ tree --noreport mysite_env/
    mysite_env/
    ├── DJANGO_SETTINGS_MODULE
    ├── DJANGO_DEBUG
    ├── DJANGO_DATABASE_URL
    ├── DJANGO_CACHE_URL
    └── PYTHONSTARTUP

    $ cat mysite_env/DJANGO_CACHE_URL
    redis://user@host:port/1

Then, to enable the ``mysite_env`` environment variables, simply use the
``envdir`` command line tool as a prefix for your program, e.g.:

.. code-block:: console

    $ envdir mysite_env python manage.py runserver

See envdir_ documentation for more information, e.g. using envdir_ from
Python instead of from the command line.

.. _envdir: https://pypi.python.org/pypi/envdir

Sentry (dynamic setup calls)
----------------------------

For all tools that require an initialization call you should use
:ref:`Setup methods<setup-methods>` (unless you want them activated
for all environments).

Intuitively you might want to add the required setup call like any
other setting:

.. code-block:: python

    class Prod(Base):
        # ...

        sentry_sdk.init("your dsn", integrations=[DjangoIntegration()])

But this will activate, in this case, Sentry even when you're running a
Dev configuration. What you should do instead, is put that code in the
``post_setup`` function. That way Sentry will only ever run when Prod
is the selected configuration:

.. code-block:: python

    class Prod(Base):
        # ...

        @classmethod
        def post_setup(cls):
            """Sentry initialization"""
            super(Prod, cls).post_setup()
            sentry_sdk.init(
                dsn=os.environ.get("your dsn"), integrations=[DjangoIntegration()]
            )


Celery
------

< 3.1
^^^^^

Given Celery's way to load Django settings in worker processes you should
probably just add the following to the **beginning** of your settings module:

.. code-block:: python

    import dj_configurator
    dj_configurator.setup()

That has the same effect as using the ``manage.py``, ``wsgi.py`` or ``asgi.py`` utilities.
This will also call ``django.setup()``.

>= 3.1
^^^^^^

In Celery 3.1 and later the integration between Django and Celery has been
simplified to use the standard Celery Python API. Django projects using Celery
are now advised to add a ``celery.py`` file that instantiates an explicit
``Celery`` client app.

Here's how to integrate django-configurator following the `example from
Celery's documentation`_:

.. code-block:: python
   :emphasize-lines: 9, 11-12

    from __future__ import absolute_import

    import os

    from celery import Celery
    from django.conf import settings

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'MySiteConfiguration')

    import dj_configurator
    dj_configurator.setup()

    app = Celery('mysite')
    app.config_from_object('django.conf:settings')
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

    @app.task(bind=True)
    def debug_task(self):
        print('Request: {0!r}'.format(self.request))

.. _`example from Celery's documentation`: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html


iPython notebooks
-----------------

.. versionadded:: 0.6

To use django-configurator with IPython_'s great notebooks, you have to
enable an extension in your IPython configuration. See the IPython
documentation for how to create and `manage your IPython profile`_ correctly.

Here's a quick how-to in case you don't have a profile yet. Type in your
command line shell:

.. code-block:: console

    $ ipython profile create

Then let IPython show you where the configuration file ``ipython_config.py``
was created:

.. code-block:: console

    $ ipython locate profile

That should print a directory path where you can find the
``ipython_config.py`` configuration file. Now open that file and extend the
``c.InteractiveShellApp.extensions`` configuration value. It may be commented
out from when IPython created the file or it may not exist in the file at all.
In either case make sure it's not a Python comment anymore and reads like this:

.. code-block:: python

   # A list of dotted module names of IPython extensions to load.
   c.InteractiveShellApp.extensions = [
       # .. your other extensions if available
       'dj_configurator',
   ]

That will tell IPython to load django-configurator correctly on startup.
It also works with django-extensions's shell_plus_ management command.

.. _IPython: http://ipython.org/
.. _`manage your IPython profile`: http://ipython.org/ipython-doc/dev/config/overview.html#configuration-file-location
.. _shell_plus: https://django-extensions.readthedocs.io/en/latest/shell_plus.html


FastCGI
-------

In case you use FastCGI for deploying Django (you really shouldn't) and aren't
allowed to use Django's runfcgi_ management command (that would automatically
handle the setup for you if you've followed the quickstart guide above), make
sure to use something like the following script:

.. code-block:: python

    #!/usr/bin/env python

    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'MySiteConfiguration')

    from dj_configurator.fastcgi import runfastcgi

    runfastcgi(method='threaded', daemonize='true')

As you can see django-configurator provides a helper module
``dj_configurator.fastcgi`` that handles the setup of your dj_configurator.

.. _runfcgi: https://docs.djangoproject.com/en/1.5/howto/deployment/fastcgi/


Sphinx
------

In case you would like to user the amazing `autodoc` feature of the
documentation tool `Sphinx <http://sphinx-doc.org/>`_, you need add
django-configurator to your ``extensions`` config variable and set
the environment variable accordingly:

.. code-block:: python
   :emphasize-lines: 2-3, 12

    # My custom Django environment variables
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

    # Add any Sphinx extension module names here, as strings. They can be extensions
    # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.viewcode',
        # ...
        'dj_configurator.sphinx',
    ]

    # ...

.. versionchanged:: 2.0

Please note that the sphinx callable has been moved from ``dj_configurator`` to
``dj_configurator.sphinx``.


Channels
--------

If you want to deploy a project that uses the Django channels with
`Daphne <http://github.com/django/daphne/>`_ as the
`interface server <http://channels.readthedocs.io/en/latest/deploying.html#run-interface-servers>`_
you have to use a asgi.py script similar to the following:

.. code-block:: python

    import os
    from dj_configurator import importer
    from channels.asgi import get_channel_layer

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

    importer.install()

    channel_layer = get_channel_layer()

That will properly load your django-configurator powered settings.
