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

extras_require = \
{'docs': ['sphinx>=2.3.1,<3.0.0',
          'sphinx-rtd-theme>=0.4.3,<0.5.0',
          'tomlkit>=0.5.8,<0.6.0']}

setup_kwargs = {
    'name': 'mobilitydb-sqlalchemy',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'B Krishna Chaitanya',
    'author_email': 'bkchaitan94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adonmo/mobilitydb-sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
