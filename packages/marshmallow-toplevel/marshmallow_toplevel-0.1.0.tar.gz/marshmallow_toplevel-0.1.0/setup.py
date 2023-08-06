# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marshmallow_toplevel']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.0.0,<4.0.0', 'pytest>=5.3.2,<6.0.0']

setup_kwargs = {
    'name': 'marshmallow-toplevel',
    'version': '0.1.0',
    'description': 'Validate top-level lists with all the power of marshmallow',
    'long_description': None,
    'author': 'Andrey Semakin',
    'author_email': 'and-semakin@ya.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
