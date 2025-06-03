"""
invokes django-cadmin when the dj_configurator module is run as a script.

Example: python -m dj_configurator check
"""

from .management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line()
