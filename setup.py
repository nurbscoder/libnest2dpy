# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libnest2dpy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'libnest2dpy',
    'version': '1.0.0',
    'description': 'Python wrapper for 2D irregular bin packaging and nesting library',
    'long_description': '# libnest2dpy\nPython wrapper for libnest2d\n',
    'author': 'Markus Frings',
    'author_email': 'markusf@moduleworks.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
