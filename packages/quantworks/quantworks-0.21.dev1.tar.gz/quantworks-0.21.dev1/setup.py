# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quantworks',
 'quantworks.barfeed',
 'quantworks.broker',
 'quantworks.dataseries',
 'quantworks.feed',
 'quantworks.optimizer',
 'quantworks.stratanalyzer',
 'quantworks.strategy',
 'quantworks.talibext',
 'quantworks.technical',
 'quantworks.tools',
 'quantworks.utils',
 'quantworks.websocket']

package_data = \
{'': ['*']}

install_requires = \
['coveralls>=1.9,<2.0',
 'matplotlib==3.1.2',
 'numpy==1.18.0',
 'python-dateutil==2.8.1',
 'pytz==2019.3',
 'requests==2.22.0',
 'retrying==1.3.3',
 'scipy==1.4.1',
 'six==1.13.0',
 'tornado==6.0.3',
 'ws4py==0.3.4']

extras_require = \
{'TALib': ['TA-Lib>=0.4.17,<0.5.0']}

setup_kwargs = {
    'name': 'quantworks',
    'version': '0.21.dev1',
    'description': 'Python Algorithmic Trading Framework',
    'long_description': None,
    'author': 'Tyler M Kontra',
    'author_email': 'tyler@tylerkontra.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
