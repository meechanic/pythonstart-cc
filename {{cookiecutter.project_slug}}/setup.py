#!/usr/bin/env python
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_slug }}',
    license="MIT",
    scripts=['bin/{{ cookiecutter.script_name }}.py'],
    packages=['{{ cookiecutter.package_name }}'],
    python_requires='>={{ cookiecutter.python_version }}',
)
