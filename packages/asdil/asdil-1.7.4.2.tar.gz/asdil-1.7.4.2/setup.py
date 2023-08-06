# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asdil']

package_data = \
{'': ['*']}

install_requires = \
['ConcurrentLogHandler>=0.9,<0.10',
 'crypto>=1.4,<2.0',
 'mailthon>=0.1,<0.2',
 'paramiko>=2.6,<3.0',
 'psutil>=5.6,<6.0',
 'pymysql-pooling>=1.0,<2.0',
 'pymysql>=0.9,<0.10',
 'rsa>=4.0,<5.0',
 'scp>=0.13,<0.14',
 'tqdm>=4.32,<5.0']

entry_points = \
{'console_scripts': ['asdil = asdil:main']}

setup_kwargs = {
    'name': 'asdil',
    'version': '1.7.4.2',
    'description': "Asdil's personal tool package",
    'long_description': '# Asdil\n我的自用库\n',
    'author': 'Asdil Fibrizo',
    'author_email': 'jpl4job@126.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Asdil/Asdil',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
