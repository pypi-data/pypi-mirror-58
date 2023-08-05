from setuptools import setup, find_packages

setup(
    name='pocketbook',
    version='0.1.1',
    description='Command line wallet application for the Fetch.ai network',
    url='https://github.com/fetchai/',
    author='Edward FitzGerald',
    author_email='edward.fitzgerald@fetch.ai',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
      'fetchai-ledger-api==1.0.0rc1',
      'toml',
      'colored',
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest'],
    },
    entry_points={
        'console_scripts': [
            'pocketbook=pocketbook.cli:main'
        ],
    },
)
