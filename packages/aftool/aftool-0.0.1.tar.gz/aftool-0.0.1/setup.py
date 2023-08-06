# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aftool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aftool',
    'version': '0.0.1',
    'description': "Asdil Fibrizo's tool",
    'long_description': "# aftool\nAsdil's tool\n",
    'author': 'Asdil Fibrizo',
    'author_email': 'jpl4job@126.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Asdil/aftool',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
