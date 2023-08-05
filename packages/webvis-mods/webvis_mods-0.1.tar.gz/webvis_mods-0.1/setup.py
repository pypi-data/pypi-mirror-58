from os import path
from setuptools import setup, find_packages

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='webvis_mods',
    version='0.1',
    license='MIT',

    packages=find_packages(),
    python_requires='>=3.7',

    author = 'Danil Lykov',
    author_email = 'lkvdan@gmail.com',

    install_requires = ['loguru', 'hosta'],
    setup_requires = ['pytest-runner'],
    tests_require  = ['pytest'],
    include_package_data=True,
    keywords = ['tools', 'webvis', 'package manager', 'data', 'framework', 'visualization'],

    long_description=long_description,
    long_description_content_type='text/markdown',

    test_suite='tests',
)
