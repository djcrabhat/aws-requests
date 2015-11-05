from setuptools import setup, find_packages
import sys

install_requires = [
    'requests',
    'boto3'
]

with open('README') as f:
    readme = f.read()

setup(
    name='awsrequests',
    version='0.0.1',
    packages=['awsrequests'],
    url='https://github.com/djcrabhat/aws-requests',
    license='djcrabhat@sosimplerecords.com',
    author='djcrabhat',
    author_email='',
    description='a requests-wrapper for AWS signed HTTP calls',
    install_requires=install_requires
)
