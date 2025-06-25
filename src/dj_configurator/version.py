import typing
from importlib.metadata import PackageNotFoundError, version

try:
    __version__: typing.Optional[str] = version("django-configurator")
except PackageNotFoundError:
    # package is not installed
    __version__ = None
