# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobilitydb_sqlalchemy', 'mobilitydb_sqlalchemy.types']

package_data = \
{'': ['*']}

install_requires = \
['geoalchemy2>=0.6.3,<0.7.0',
 'pandas>=0.25.3,<0.26.0',
 'shapely>=1.6.4,<2.0.0',
 'sqlalchemy>=1.3.11,<2.0.0']

setup_kwargs = {
    'name': 'mobilitydb-sqlalchemy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'B Krishna Chaitanya',
    'author_email': 'bkchaitan94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adonmo/mobilitydb_sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
