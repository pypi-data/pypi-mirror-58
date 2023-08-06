# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pyfabrik']

package_data = \
{'': ['*']}

install_requires = \
['vectormath>=0.2.2,<0.3.0']

setup_kwargs = {
    'name': 'pyfabrik',
    'version': '0.2.0',
    'description': 'Python 3 implementation of FABRIK (Forward And Backward Reaching Inverse Kinematics) algorithm.',
    'long_description': '# pyfabrik\n\n![Badge showing number of total downloads from PyPI.](https://pepy.tech/badge/pyfabrik)\n\n![Badge showing number of monthly downloads from PyPI.](https://pepy.tech/badge/pyfabrik/month)\n\n![Badge showing that code has been formated with Black formatter.](https://img.shields.io/badge/code%20style-black-000000.svg)\n\nPython 3 implementation of\n[FABRIK](http://www.andreasaristidou.com/FABRIK.html) (Forward And\nBackward Reaching Inverse Kinematics).\n## Installation\n\n    pip install pyfabrik\n\n## Goal\n![Inverse kinematics example with human skeleton.](http://www.andreasaristidou.com/publications/images/FABRIC_gif_1.gif)\n\n## Roadmap\n\n- [x] Basic 2D (flat chain)\n- [x] Basic 3D (flat chain)\n- [ ] 3D testing sandbox\n- [ ] Basic 2D joint movement restrictions\n- [ ] Basic 3D joint movement restrictions\n- [ ] Complex chain support 2D\n- [ ] Complex chain support 3D\n\n## Contributing\n\n__All contributions are appreciated.__\n\nYou can find almost everything you need in the [paper](http://www.andreasaristidou.com/publications/papers/FABRIK.pdf).\nOn FABRIKs [homepage](http://www.andreasaristidou.com/FABRIK.html) you can find examples and links to other implementations.\n\n## License\n[GNU GENERAL PUBLIC LICENSE Version 3](./LICENSE)\n',
    'author': 'Saša Savić',
    'author_email': 'sasa@savic.one',
    'url': 'https://github.com/saleone/pyfabrik',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
