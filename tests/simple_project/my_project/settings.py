from dj_configurator import Configuration, values


class Base(Configuration):
    # Django settings for my_project project.

    DEBUG = values.BooleanValue(True, environ=True)

    ADMINS = (
        # ('Your Name', 'your_email@example.com'),
    )

    EMAIL_URL = values.EmailURLValue("console://", environ=True)

    MANAGERS = ADMINS

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            "NAME": "",  # Or path to database file if using sqlite3.
            "USER": "",  # Not used with sqlite3.
            "PASSWORD": "",  # Not used with sqlite3.
            "HOST": "",  # Set to empty string for localhost. Not used with sqlite3.
            "PORT": "",  # Set to empty string for default. Not used with sqlite3.
        }
    }

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = []

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = "America/Chicago"

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = "en-us"

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ""

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ""

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = ""

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = "/static/"

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = "-9i$j8kcp48(y-v0hiwgycp5jb*_)sy4(swd@#m(j1m*4vfn4w"

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    )

    MIDDLEWARE = (
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = "my_project.urls"

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = "my_project.wsgi.application"

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    INSTALLED_APPS = (
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # Uncomment the next line to enable the admin:
        # 'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        "dj_configurator",
    )

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
        },
        "handlers": {
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"],
                "class": "django.utils.log.AdminEmailHandler",
            }
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        },
    }


class Debug(Base):
    YEAH = True


class Other(Base):
    YEAH = False
