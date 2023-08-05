# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['longhow']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.0.5,<3.0.0']

setup_kwargs = {
    'name': 'longhow',
    'version': '0.1.0',
    'description': 'A simple decorator to measure a function execution time',
    'long_description': 'how_long\n========\n\nSimple Decorator to measure a function execution time.\n\nExample\n_______\n\n.. code-block:: python\n\n    from longhow import timer\n\n\n    @timer\n    def some_function():\n        return [x for x in range(10_000_000)]',
    'author': 'Tendi Muchenje',
    'author_email': 'tendi@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
