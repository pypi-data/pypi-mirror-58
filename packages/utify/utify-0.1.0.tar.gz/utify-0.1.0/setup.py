# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['utify']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0',
 'ipython>=7.10.2,<8.0.0',
 'matplotlib>=3.1.2,<4.0.0',
 'numpy>=1.17.4,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'pillow>=6.2.1,<7.0.0',
 'pyarrow>=0.15.1,<0.16.0',
 'seaborn>=0.9.0,<0.10.0',
 'sqlalchemy>=1.3.12,<2.0.0',
 'tqdm>=4.40.2,<5.0.0',
 'wasabi>=0.4.2,<0.5.0']

entry_points = \
{'console_scripts': ['utify = utify.cli:main']}

setup_kwargs = {
    'name': 'utify',
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
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
