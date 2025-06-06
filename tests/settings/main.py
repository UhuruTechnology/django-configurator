import os
import uuid

from dj_configurator import Configuration, pristinemethod


class Test(Configuration):
    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
    )

    DEBUG = True

    SITE_ID = 1

    SECRET_KEY = str(uuid.uuid4())

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(os.path.dirname(__file__), "test.db"),
        }
    }

    INSTALLED_APPS = [
        "django.contrib.sessions",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "django.contrib.auth",
        "tests",
    ]

    ROOT_URLCONF = "tests.urls"

    @property
    def ALLOWED_HOSTS(self):
        allowed_hosts = super().ALLOWED_HOSTS[:]
        allowed_hosts.append("base")
        return allowed_hosts

    ATTRIBUTE_SETTING = True

    _PRIVATE_SETTING = "ryan"

    @property
    def PROPERTY_SETTING(self):
        return 1

    def METHOD_SETTING(self):
        return 2

    LAMBDA_SETTING = lambda self: 3  # noqa: E731

    PRISTINE_LAMBDA_SETTING = pristinemethod(lambda: 4)

    @pristinemethod
    def PRISTINE_FUNCTION_SETTING():
        return 5

    @classmethod
    def pre_setup(cls):
        cls.PRE_SETUP_TEST_SETTING = 6

    @classmethod
    def post_setup(cls):
        cls.POST_SETUP_TEST_SETTING = 7


class TestWithDefaultSetExplicitely(Test):
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
