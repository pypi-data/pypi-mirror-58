from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kumaoche',
    version='0.1.24',
    description='Pythonic Dev Repository & Dev Environment Management tool.',
    long_description='',
    author='kumak1',
    author_email='kumaki0@gmail.com',
    install_requires=['invoke', 'pyyaml'],
    url='https://github.com/kumak1/kumaoche',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    test_suite='tests'
)
