"""
Flask SocketIO Bootstrap 4 Boilerplate
"""

import re
from setuptools import setup

with open('app/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='UvA Intelligent Robotics website',
    version=version,
    url='https://github.com/uva-robotics/website',
    license='MIT',
    author='Janne Spijkervet',
    author_email='janne.spijkervet@hotmail.com',
    description='UvA Intelligent robotics website',
    long_description=__doc__,
    packages=[''],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'python-socketio>=1.6.1'
    ]
)
