from setuptools import setup

install_requires = [
    'requests',
    'boto3'
]

with open('README.rst') as f:
    readme = f.read()

setup(
    name='awsrequests',
    version='0.0.13',
    packages=['awsrequests'],
    url='https://github.com/djcrabhat/aws-requests',
    license='MIT License',
    author='ClearDATA',
    author_email='support@cleardata.com',
    description='For making signed requests to AWS API Gateway endpoints',
    install_requires=install_requires,
    keywords=['AWS API Gateway signing', 'API Gateway signing', 'AWS API Gateway requests', 'API Gateway requests'],
    classifiers=[],
)
