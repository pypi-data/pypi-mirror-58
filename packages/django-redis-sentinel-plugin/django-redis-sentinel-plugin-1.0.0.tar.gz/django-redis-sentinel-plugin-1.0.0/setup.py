# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_redis_sentinel_plugin', 'django_redis_sentinel_plugin.client']

package_data = \
{'': ['*']}

install_requires = \
['django-redis>=4.10.0,<5.0.0', 'django>=2.2.6,<3.0.0', 'redis>=3.3.11,<4.0.0']

setup_kwargs = {
    'name': 'django-redis-sentinel-plugin',
    'version': '1.0.0',
    'description': 'django-redis plugin that supports Sentinel Cluster HA',
    'long_description': '# Django-Redis Client that supports Sentinel Cluster HA\n\n本仓库基于: [django-redis-sentinel](https://github.com/danigosa/django-redis-sentinel-redux)\n进行了更新.\n比如删除了老旧代码.后面随着自己的使用可能也会继续的更新.\n',
    'author': 'banxi1988',
    'author_email': 'banxi1988@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
