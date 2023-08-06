# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_bgm_api', 'async_bgm_api.models']

package_data = \
{'': ['*']}

install_requires = \
['httpx==0.9.5', 'pydantic>=1.2,<2.0']

setup_kwargs = {
    'name': 'async-bgm-api',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Trim21',
    'author_email': 'i@trim21.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
