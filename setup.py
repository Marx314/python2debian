from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python2debian',
    packages=['python2debian'],
    version='0.0.1',
    description='Python 2 Debian',
    long_description=readme,
    author='Internap Hosting',
    author_email='opensource@internap.com',
    url='https://github.com/internap/python2debian',
    license=license,
    install_requires=['Jinja2==2.9.6'],
    entry_points={
        'console_scripts': [
            'python2debian = python2debian.main:main'
        ]
    },
)
