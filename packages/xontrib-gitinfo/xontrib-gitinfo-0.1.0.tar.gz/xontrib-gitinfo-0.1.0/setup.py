# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xontrib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xontrib-gitinfo',
    'version': '0.1.0',
    'description': 'Displays information on entering a git repository.',
    'long_description': '# xontrib-gitinfo\n\nDisplays git information on entering a repository folder.\nUses [onefetch](https://github.com/o2sh/onefetch) if available.\n\n## Requirements\n\n- Python 3.7+ (might work with older version as well)\n- [xonsh](https://xon.sh/)\n- [optional] [onefetch](https://github.com/o2sh/onefetch)\n\n## Install\n\n```\n$ pip install xontrib-gitinfo\n$ xontrib load gitinfo\n```\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dyuri/xontrib-gitinfo',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
