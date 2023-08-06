# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['messagemedia_simple']

package_data = \
{'': ['*']}

install_requires = \
['tox>=3.14,<4.0']

setup_kwargs = {
    'name': 'messagemedia-simple',
    'version': '0.1.1',
    'description': 'Simple MessageMedia module for sending SMS messages.',
    'long_description': '# Simple MessageMedia API wrapper\n\nSimple and easy to use module for sending SMS and MMS messages through MessageMedia.com API.\n\n## Author\n\nMichael Ludvig <mludvig@logix.net.nz>\n',
    'author': 'Michael Ludvig',
    'author_email': 'mludvig@logix.net.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mludvig/messagemedia-simple',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
