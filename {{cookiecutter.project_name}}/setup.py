#!/usr/bin/python3

import io
import os
import sys

from setuptools import setup

# Package meta-data.
NAME = '{{cookiecutter.project_name}}'
DESCRIPTION = 'My short description for my project.'
URL = 'https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}'
EMAIL = '{{cookiecutter.author_email}}'
AUTHOR = '{{cookiecutter.author_name}}'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '0.0.1-pre'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'numpy', 'requests', 'uncertainties',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec (f.read(), about)
else:
about['__version__'] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['{{cookiecutter.project_name}}'],
    entry_points={
        'console_scripts': ['{{cookiecutter.project_name}}={{cookiecutter.project_name}}:main'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='{{cookiecutter.license}}',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        {%- if cookiecutter.license == "MIT" %}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == "GPLv3" %}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- endif %}
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 3 - Alpha'
    ],
)
