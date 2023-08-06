# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docx2pdf']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.41.0,<5.0.0']

extras_require = \
{':sys_platform == "win32"': ['pywin32>=227,<228']}

entry_points = \
{'console_scripts': ['docx2pdf = docx2pdf:cli']}

setup_kwargs = {
    'name': 'docx2pdf',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Al Johri',
    'author_email': 'al.johri@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
