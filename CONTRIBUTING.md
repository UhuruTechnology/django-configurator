Setting Up Development Environment
==================================
NOTE: Assumes git is already installed on your system.

Install uv if not already on your system:
https://docs.astral.sh/uv/getting-started/installation/

Install Python versions you want to develop with:

uv python install 3.11 3.12

Pin the base Python version you want to use:
uv python pin 3.12

Setting up test tool
uv tool install tox --with tox-uv # use uv to install

Sync the environment:
uv sync

Running tests:
make test

Formatting files:
make format