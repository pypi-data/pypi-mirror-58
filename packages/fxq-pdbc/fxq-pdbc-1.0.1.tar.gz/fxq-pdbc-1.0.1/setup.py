import pathlib

from setuptools import setup

setup(
    name='fxq-pdbc',
    version='1.0.1',
    packages=[
        'fxq'
    ],
    url='https://bitbucket.org/fxqlabs-oss/fxq-pdbc/',
    license='MIT',
    author='Jonathan Turnock',
    author_email='jonathan.turnock@outlook.com',
    description='',
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=['pyodbc', 'multipledispatch']
)
