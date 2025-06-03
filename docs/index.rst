.. include:: ../README.rst

Okay, how does it work?
-----------------------

Any subclass of the ``dj_configurator.Configuration`` class will automatically
use the values of its class and instance attributes (including properties
and methods) to set module level variables of the same module -- that's
how Django will interface to the django-configurator based settings during
startup and also the reason why it requires you to use its own startup
functions.

That means when Django starts up django-configurator will have a look at
the ``DJANGO_CONFIGURATION`` environment variable to figure out which class
in the settings module (as defined by the ``DJANGO_SETTINGS_MODULE``
environment variable) should be used for the process. It then instantiates
the class defined with ``DJANGO_CONFIGURATION`` and copies the uppercase
attributes to the module level variables.

Alternatively you can use the ``--configuration`` command line option that
django-configurator adds to all Django management commands. Behind the
scenes it will simply set the ``DJANGO_CONFIGURATION`` environment variable
so this is purely optional and just there to compliment the default
``--settings`` option that Django adds if you prefer that instead of setting
environment variables.

But isn't that magic?
---------------------

Yes, it looks like magic, but it's also maintainable and non-intrusive.
No monkey patching is needed to teach Django how to load settings via
django-configurator because it uses Python import hooks (`PEP 302`_)
behind the scenes.

.. _`PEP 302`: http://www.python.org/dev/peps/pep-0302/

Further documentation
---------------------

.. toctree::
   :maxdepth: 3

   patterns
   values
   cookbook
   changes

Alternatives
------------

Many thanks to those project that have previously solved these problems:

- The Pinax_ project for spearheading the efforts to extend the Django
  project metaphor with reusable project templates and a flexible
  configuration environment.

- `django-classbasedsettings`_ by Matthew Tretter for being the immediate
  inspiration for django-configurator.

.. _Pinax: http://pinaxproject.com
.. _`django-classbasedsettings`: https://github.com/matthewwithanm/django-classbasedsettings

- `django-configurations`_ Jannis Leidel was the original creator and eventually the project
  was adopted by Jazzband but became defunct due to lack of project management and resurrected
  and modernised the original projects tools and packaging here.
 
.. _`django-configurations`: https://github.com/jazzband/django-configurations


Bugs and feature requests
-------------------------

As always your mileage may vary, so please don't hesitate to send feature
requests and bug reports:

- https://github.com/UhuruTechnology/django-configurator/issues

Thanks!
