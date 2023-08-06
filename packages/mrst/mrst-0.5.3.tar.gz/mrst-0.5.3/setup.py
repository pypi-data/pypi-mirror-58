# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mrst']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=2.3.1,<3.0.0', 'typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['mrst = mrst.cli:main']}

setup_kwargs = {
    'name': 'mrst',
    'version': '0.5.3',
    'description': '',
    'long_description': None,
    'author': 'Tim Simpson',
    'author_email': 'timsimpson4@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
