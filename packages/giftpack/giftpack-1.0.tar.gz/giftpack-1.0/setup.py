# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['giftpack',
 'giftpack.commands',
 'giftpack.events',
 'giftpack.stars',
 'giftpack.tables']

package_data = \
{'': ['*']}

install_requires = \
['royalnet[telegram,discord,matrix,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]>=5.2,<6.0']

setup_kwargs = {
    'name': 'giftpack',
    'version': '1.0',
    'description': 'A pack for the gift drawing at the Xmas 2019 family lunch',
    'long_description': '# `giftpack`\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'ste.pigozzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Steffo99/giftpack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
