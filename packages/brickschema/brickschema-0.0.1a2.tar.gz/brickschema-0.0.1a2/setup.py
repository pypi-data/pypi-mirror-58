# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['brickschema']

package_data = \
{'': ['*'], 'brickschema': ['ontologies/*']}

install_requires = \
['owlrl>=5.2,<6.0', 'rdflib>=4.2,<5.0']

setup_kwargs = {
    'name': 'brickschema',
    'version': '0.0.1a2',
    'description': 'A library for working with the Brick ontology for buildings (brickschema.org)',
    'long_description': None,
    'author': 'Gabe Fierro',
    'author_email': 'gtfierro@cs.berkeley.edu',
    'url': 'https://brickschema.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
