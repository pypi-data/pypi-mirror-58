from setuptools import setup, find_packages

setup(
    name='consumer_helper',
    version='0.1.0',
    description='help user to complete data processing when process receive SIGTERM. only for simple processing logic.',
    author='Jerry',
    packages=['consumer_helper'],
    install_requires=['confluent-kafka', 'configargparse']
)
