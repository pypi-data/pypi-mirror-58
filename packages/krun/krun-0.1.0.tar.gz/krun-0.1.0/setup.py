# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['krun']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'krun',
    'version': '0.1.0',
    'description': 'A http test library, inspired by httprunner.',
    'long_description': None,
    'author': 'ready',
    'author_email': '791100944@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
