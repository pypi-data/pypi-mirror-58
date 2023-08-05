# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kangry_pomodoro']

package_data = \
{'': ['*']}

modules = \
['icon']
install_requires = \
['click>=7.0,<8.0',
 'dbus-python>=1.2,<2.0',
 'notify2>=0.3.1,<0.4.0',
 'pyqt5>=5.13,<6.0']

entry_points = \
{'console_scripts': ['pomodoro = kangry_pomodoro.app:main']}

setup_kwargs = {
    'name': 'kangry-pomodoro',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Gregory',
    'author_email': 'netsafe.g@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
