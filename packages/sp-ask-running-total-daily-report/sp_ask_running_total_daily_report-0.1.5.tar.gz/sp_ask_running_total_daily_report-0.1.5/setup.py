# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sp_ask_running_total_daily_report']

package_data = \
{'': ['*']}

install_requires = \
['XlsxWriter>=1.2,<2.0',
 'ask_academic_dates>=0.2.3,<0.3.0',
 'ask_schools>=0.2.4,<0.3.0',
 'lh3api>=0.2.0,<0.3.0',
 'pandas>=0.25.3,<0.26.0',
 'pdbpp>=0.10.2,<0.11.0',
 'xlrd>=1.2,<2.0']

setup_kwargs = {
    'name': 'sp-ask-running-total-daily-report',
    'version': '0.1.5',
    'description': 'An helper that create and Excel document representing the number of chats per day',
    'long_description': None,
    'author': 'Guinsly Mondesir',
    'author_email': 'guinslym@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
