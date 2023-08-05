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
    'version': '0.1.6',
    'description': 'An helper that create and Excel document representing the number of chats per day',
    'long_description': "# SP Ask Running Total Daily report\nAn helper that create and Excel document representing the number of chats per day. Which are on the Daily Spreadsheet\n\n### Installation\n\n    $ pip install sp_ask_running_total_daily_report\n    $ or with poetry\n    $ poetry add sp_ask_running_total_daily_report\n\n### Utilisation\n```python\nfrom sp_ask_running_total_daily_report import create_report\n\n# generating stats for a given month (february)\ncreate_report(2019, 2)\n\n#generating stats for all months\nfor month_number in range(1, 13):\n    create_report(2019, month_number)\n```\nWill create a file **'2-February.xlsx'** on the current directory\n\n### Screenshot\nThis is a screenshot. We don't provide our daily stats to the public. The number below were updated to fake our real numbers.\n![screenshot of app](screenshots/screenshot3.png)\n\n\n### Todo\n1.  Test\n2.  Refactor\n3.  Add docstring\n4.  Add a Makefile\n5.  Add show terminal graph for a given month\n6.  Create a .rst file and add metadata for \n",
    'author': 'Guinsly Mondesir',
    'author_email': 'guinslym@gmail.com',
    'url': 'https://github.com/guinslym/sp_ask_running_total_daily_report',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
