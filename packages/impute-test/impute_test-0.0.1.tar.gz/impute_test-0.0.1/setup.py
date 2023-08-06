# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impute_test']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.0,<2.0.0']

setup_kwargs = {
    'name': 'impute-test',
    'version': '0.0.1',
    'description': '测试poetry上传到pipy',
    'long_description': '# impute_test\n打包到pipy的示例\n',
    'author': 'Asdil',
    'author_email': 'fake_add@126.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Asdil/impute_test',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
