from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qdds',
    version='1.1.2',
    description='Quick Django Dev Server shortcut using your IP and port 8000',
    long_description=long_description,
    author = 'benmcnelly',
    author_email = 'me@benmcnelly.com',
    url = 'https://github.com/benmcnelly/qdds',
    py_modules=['devserver'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        devserver=devserver:cli
    ''',
)
