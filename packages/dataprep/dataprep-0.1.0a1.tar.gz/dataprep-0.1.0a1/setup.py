# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataprep',
 'dataprep.data_connector',
 'dataprep.eda',
 'dataprep.eda.basic',
 'dataprep.eda.correlation',
 'dataprep.eda.missing',
 'dataprep.eda.outlier',
 'dataprep.tests',
 'dataprep.tests.eda']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=1.4,<1.5',
 'dask[complete]>=2.9,<2.10',
 'holoviews>=1.12,<1.13',
 'jinja2>=2.10,<2.11',
 'jsonpath2>=0.4,<0.5',
 'jsonschema>=3.1,<3.2',
 'lxml>=4.4,<4.5',
 'numpy>=1.17,<1.18',
 'pandas>=0.25,<0.26',
 'probscale>=0.2,<0.3',
 'requests>=2.22,<2.23',
 'scipy>=1.3,<1.4']

setup_kwargs = {
    'name': 'dataprep',
    'version': '0.1.0a1',
    'description': 'Dataprep is a library to help data scientist accomplish all the tasks using one library before building the predictive model.',
    'long_description': "# DataPrep ![Build Status]\n\nDataPrep is a library to greatly save data scientists' time.\n\n[Documentation]\n\n# Contribution guidelines\nIf you want to contribute to DataPrep, be sure to review the [contribution guidelines](CONTRIBUTING.md).\n\n\n\n[Build Status]: https://img.shields.io/circleci/build/github/sfu-db/dataprep/master?style=flat-square&token=f68e38757f5c98771f46d1c7e700f285a0b9784d\n[Documentation]: https://sfu-db.github.io/dataprep/\n",
    'author': 'Weiyuan Wu',
    'author_email': 'youngw@sfu.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sfu-db/dataprep',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
