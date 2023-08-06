from setuptools import setup

from meraxes.finance import __version__


setup(
    name='meraxes.finance',
    version=__version__,

    author='Stefan Bunde',
    author_email='stefanbunde+git@gmail.com',

    packages=['meraxes.finance', 'meraxes.finance.migrations'],

    install_requires=[
        'Django>=2',
        'djangorestframework>=3.8',
    ],
    extras_require={
        'release': [
            'twine',
        ],
        'testing': [
            'tox',
        ],
    },
)
