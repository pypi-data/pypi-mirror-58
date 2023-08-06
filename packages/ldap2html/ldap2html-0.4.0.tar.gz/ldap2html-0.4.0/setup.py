# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ldap2html',
 'ldap2html.html',
 'ldap2html.html2ldif',
 'ldap2html.ldap',
 'ldap2html.ldap2html']

package_data = \
{'': ['*']}

install_requires = \
['ldap3>=2.6,<3.0']

entry_points = \
{'console_scripts': ['html2ldif = ldap2html.html2ldif:main',
                     'ldap2html = ldap2html.ldap2html:main']}

setup_kwargs = {
    'name': 'ldap2html',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'nonylene',
    'author_email': 'nonylene@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nonylene/ldap2html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
