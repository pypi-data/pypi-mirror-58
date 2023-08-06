# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['imperial_dateutil', 'imperial_dateutil.core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'imperial-dateutil',
    'version': '0.1.0',
    'description': 'Utility for imperial dating system that supports both era indomitus system and original system',
    'long_description': '# imperial-dateutil\nUtility for imperial dating system that supports both era indomitus system and original system\n',
    'author': 'Seonghyeon Kim',
    'author_email': 'kim@seonghyeon.dev',
    'url': 'https://github.com/NovemberOscar/imperial-dateutil',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
