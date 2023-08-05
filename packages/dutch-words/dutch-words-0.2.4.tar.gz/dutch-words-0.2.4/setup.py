# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dutch_words']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dutch-words',
    'version': '0.2.4',
    'description': '',
    'long_description': '=========================================================\nDutch word list\n=========================================================\nA simple python package that exports a list of almost 10,000 Dutch words ranked by usage.\n\nUsage\n=====\n::\n\n    import dutch_words\n    words = dutch_words.get_ranked()\n\nThanks\n======\nThanks to `Sasha Romijn <https://github.com/mxsasha>`_ for the inspiration and the University of\nLeipzig for the `Dutch word list <http://wortschatz.uni-leipzig.de/en/download/>`_.\n\nLicense\n=======\nThe word list provided by the University of Leipzig and the python code are available under the `CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_ license.\n',
    'author': 'Ramon de Jezus',
    'author_email': 'rdejezus@leukeleu.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/leukeleu/dutch-words',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
