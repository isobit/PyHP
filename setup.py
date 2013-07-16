# T37 Library

from distutils.core import setup
import os

def get_location():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep

def cd_here():
    os.chdir(get_location())

cd_here()

setup(
    name='PyHP',
    version='0.1',
    author='Josh Glendenning',
    author_email='joshglendenning@gmail.com',
    packages=['pyhp'],
    description='Class for using PHP-like <?py ?> tags in HTML templates.',
)

