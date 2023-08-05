#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()


with open('HISTORY.md') as history_file:
    history = history_file.read()


requirements = ['pydantic>=1.2']


setup(
    author="Kelton Karboviak",
    author_email='kelton.karboviak@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Pydantic models for AWS Events",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='AWS Lambda Pydantic',
    name='aws-lambda-event-models',
    packages=find_packages(include=['aws_lambda_event_models', 'aws_lambda_event_models.*']),
    url='https://github.com/KeltonKarboviak/aws-lambda-event-models',
    version='0.0.0',
    zip_safe=False,
)
