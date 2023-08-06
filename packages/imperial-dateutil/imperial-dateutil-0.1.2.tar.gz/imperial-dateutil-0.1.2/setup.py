# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['imperial_dateutil', 'imperial_dateutil.core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'imperial-dateutil',
    'version': '0.1.2',
    'description': 'Utility for imperial dating system that supports both era indomitus system and original system',
    'long_description': '<p align="center">\n  <img src=https://vignette.wikia.nocookie.net/warhammer40k/images/3/3f/IoMhighres.png/revision/latest/scale-to-width-down/620?cb=20190630130844 />\n</p>\n\n<h1 align="center"> imperial-dateutil </h1>\n\n<img align="right" src=https://giantbomb1.cbsistatic.com/uploads/original/1/17172/1415053-imperium_036.jpg height=300>\n\nA utility to use Imperial Dating System(include Era Indomitus Dating System)\n\n> The Emperor protects always and forever. He is the Omnissiah and will always live, always protect, always watch. He will protect all loyal to the Imperium and it is an honor to fight and die in the name of the emperor.\n\n```\npip install imperial-dateutil\n```\n\n## Documentation\n[Here is the documentation](https://imperial-dateutil.readthedocs.io/en/latest/)\n\n## Features\n- Original Imperial Dating System\n- Era Indomitus Dating System\n\n## Prerequesties\n- Belief to The Emperor, the Omnisiah\'s avatar\n- A little ability of Lingua-technis and row gothic\n\n---\n\n> GW, Games Workshop, Citadel, Black Library, Forge World, Warhammer, the Twin-tailed Comet logo, Warhammer 40,000, the ‘Aquila’ Double-headed Eagle logo, Space Marine, 40K, 40,000, Warhammer Age of Sigmar, Battletome, Stormcast Eternals, White Dwarf, Blood Bowl, Necromunda, Space Hulk, Battlefleet Gothic, Dreadfleet, Mordheim, Inquisitor, Warmaster, Epic, Gorkamorka, and all associated logos, illustrations, images, names, creatures, races, vehicles, locations, weapons, characters, and the distinctive likenesses thereof, are either ® or TM, and/or © Games Workshop Limited, variably registered around the world. All Rights Reserved.',
    'author': 'Seonghyeon Kim',
    'author_email': 'kim@seonghyeon.dev',
    'url': 'https://github.com/NovemberOscar/imperial-dateutil',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
