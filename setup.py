from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='scopeARprinter',
    version='0.1.0',
    description='Ascii Printer package for scopeAR',
    long_description=readme,
    author='Dennis Truong',
    author_email='dtruong1@ualberta.ca',
    url='https://github.com/dt9/dennis_scope',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

