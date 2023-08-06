# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybtex_author_year_label']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0', 'pybtex>=0.22.2,<0.23.0', 'pytest-mock>=1.13.0,<2.0.0']

entry_points = \
{'pybtex.style.labels': ['author_year = pybtex_author_year_label:LabelStyle']}

setup_kwargs = {
    'name': 'pybtex-author-year-label',
    'version': '0.1.2',
    'description': 'Defines an author-year inline citation style for Pybtex.',
    'long_description': 'Defines an author-year inline citation style for Pybtex. This is\nmodified from the alpha style built into Pybtex, written by\nAndrey Golovizin.\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pybtex-author-year-label',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
