import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)

version_contents = {}
with open(os.path.join(cwd, 'rehook', 'version.py')) as f:
    exec(f.read(), version_contents)

setup(
    name='rehook',
    version=version_contents['VERSION'],
    packages=['rehook', ],
    url='https://github.com/punihaol/rehook',
    license='MIT',
    author='Thomas Punihaole',
    author_email='tom.punihaole@gmail.com',
    description='Saves and replays webhooks for development testing.',
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['django>=2.2', 'psycopg2-binary', 'djangorestframework>=3.10', ],
    project_urls={
        'Documentation': 'https://github.com/punihaol/rehook',
        'Source Code': 'https://github.com/punihaol/rehook',
    },
)
