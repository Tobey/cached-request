import sys

from setuptools import setup


if sys.version_info < (3, 6, 1):
    sys.exit('Python < 3.6.1 is not supported')

setup(
    name='ueniapi',
    version='0.0.1',
    packages=['ueniapi'],
    url='',
    license='UENI Internal',
    author='tobey',
    author_email='tobey@ueni.com',
    description='',
    install_requires=[
        'requests==2.18.2',
        'requests-cache==0.4.13',
    ]
)
