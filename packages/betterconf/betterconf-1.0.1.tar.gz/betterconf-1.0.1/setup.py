# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betterconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'betterconf',
    'version': '1.0.1',
    'description': 'Python configs for humans. Using OS environment.',
    'long_description': '# Python configs for humans.\n> Using OS environment.\n\nBefore you ask - this library doesn\'t support type-casts and other features. Just env parsing.\n\n## How to?\nAt first, install libary:\n\n```sh\npip install betterconf\n```\n\nAnd... write simple config:\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var")\n\ncfg = MyConfig()\nprint(cfg.my_var)\n```\n\nTry to run:\n```sh\nmy_var=1 python our_file.py\n```',
    'author': 'prostomarkeloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.1,<4.0',
}


setup(**setup_kwargs)
