from setuptools import setup

from meraxes.finance import __version__


setup(
    name='meraxes.finance',
    version=__version__,

    author='Stefan Bunde',
    author_email='stefanbunde+git@gmail.com',

    packages=['meraxes.finance'],

    extras_require={
        'release': [
            'twine',
        ],
    },
)
