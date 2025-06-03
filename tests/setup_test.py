"""Used by tests to ensure logging is kept when calling setup() twice."""

from unittest import mock

import dj_configurator

print("setup_1")
dj_configurator.setup()

with mock.patch("django.setup", side_effect=Exception("setup called twice")):
    print("setup_2")
    dj_configurator.setup()

print("setup_done")
