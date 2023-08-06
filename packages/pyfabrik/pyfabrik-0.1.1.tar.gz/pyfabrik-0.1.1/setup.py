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
    'version': '0.1.1',
    'description': 'Python 3 implementation of FABRIK (Forward And Backward Reaching Inverse Kinematics) algorithm.',
    'long_description': 'pyfabrik\n========\n\n  NOTE: Library is still in the early phase of development.\n\nPython 3 implementation of `FABRIK <http://www.andreasaristidou.com/FABRIK.html>`_ (Forward And Backward Reaching Inverse Kinematics).\n\n.. image:: http://www.andreasaristidou.com/publications/images/FABRIC_gif_1.gif\n   :alt: Inverse kinematics example with human skeleton\n\nInstallation\n------------\n\n::\n\n\tpip install pyfabrik\n\nImplementation\n--------------\n- Basic 2D implementation - DONE\n- Joint movement restrictions in 2D\n- Basic 3D implementation\n- Joint movement restriction in 3D\n\nContributing\n------------\nAll contributions are appreciated. You can find almost everything you need in the `paper <http://www.andreasaristidou.com/publications/papers/FABRIK.pdf>`_\nand on FABRIKs `homepage <http://www.andreasaristidou.com/FABRIK.html>`_ you can find examples and links to other implementations.\n',
    'author': 'Saša Savić',
    'author_email': 'sasa@savic.one',
    'url': 'https://github.com/saleone/pyfabrik',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
