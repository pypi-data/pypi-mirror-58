import ast
import re
import os

from setuptools import setup, find_packages

PACKAGE_NAME = 'forecastflow'

with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

setup(
    # metadata
    name=PACKAGE_NAME,
    version=version,
    description='ForecastFlow Python API',
    long_description='ForecastFlow Python API',
    author='GRI, Inc',
    author_email='forecastflow@gri.jp',
    url='https://gri.jp',
    lisense='Apache Software License',

    # options
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6.0',
    install_requires=[
        'pandas',
        'requests',
        'toml'
    ]
)
