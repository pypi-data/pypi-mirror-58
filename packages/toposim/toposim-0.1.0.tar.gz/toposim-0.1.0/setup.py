# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['toposim']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.10.2,<8.0.0',
 'numpy>=1.17.4,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'scikit-learn>=0.22,<0.23',
 'seaborn>=0.9.0,<0.10.0',
 'torch>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'toposim',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'yajiez',
    'author_email': 'yajiez.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
