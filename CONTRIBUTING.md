Setting Up Development Environment
==================================
NOTE: Assumes git is already installed on your system.

Clone the project from github:
 git clone https://github.com/UhuruTechnology/django-configurator.git

Install uv if not already on your system:
 https://docs.astral.sh/uv/getting-started/installation/

Create the development environment by running this command from the project root:
 make develop


Install Python versions you want to develop with:
 uv python install 3.11 3.12

Pin the base Python version you want to use:
 uv python pin 3.12

Running tests:
 make test

Formatting files:
 make format