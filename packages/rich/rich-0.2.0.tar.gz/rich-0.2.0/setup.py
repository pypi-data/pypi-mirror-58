# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich']

package_data = \
{'': ['*']}

install_requires = \
['pprintpp>=0.4.0,<0.5.0', 'typing-extensions>=3.7.4,<4.0.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8']}

setup_kwargs = {
    'name': 'rich',
    'version': '0.2.0',
    'description': 'Render rich text, tables, syntax highlighting, markdown and more to the terminal',
    'long_description': None,
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
