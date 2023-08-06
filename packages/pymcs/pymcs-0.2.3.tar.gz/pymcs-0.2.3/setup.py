# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymcs']

package_data = \
{'': ['*']}

install_requires = \
['cx_Oracle>=7.3.0,<8.0.0', 'pandas>=0.25.3,<0.26.0', 'tqdm>=4.41.0,<5.0.0']

setup_kwargs = {
    'name': 'pymcs',
    'version': '0.2.3',
    'description': 'Python Tools for MRO MCS data analysis',
    'long_description': '=====\npymcs\n=====\n\n\n.. image:: https://img.shields.io/pypi/v/pymcs.svg\n        :target: https://pypi.python.org/pypi/pymcs\n\n.. image:: https://img.shields.io/travis/michaelaye/pymcs.svg\n        :target: https://travis-ci.org/michaelaye/pymcs\n\n.. image:: https://readthedocs.org/projects/pymcs/badge/?version=latest\n        :target: https://pymcs.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n.. image:: https://pyup.io/repos/github/michaelaye/pymcs/shield.svg\n     :target: https://pyup.io/repos/github/michaelaye/pymcs/\n     :alt: Updates\n\n\nPython tools for MRO MCS data analysis\n\n\n* Free software: MIT license\n* Documentation: https://pymcs.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n---------\n\nThis package was created with Cookiecutter_ and the forked `michaelaye/cookiecutter-pypackage-conda`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`michaelaye/cookiecutter-pypackage-conda`: https://github.com/michaelaye/cookiecutter-pypackage-conda\n',
    'author': 'K.-Michael Aye',
    'author_email': 'kmichael.aye@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/michaelaye/pymcs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
