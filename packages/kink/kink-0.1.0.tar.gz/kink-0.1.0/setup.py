# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kink', 'kink.errors', 'kink.resolvers']

package_data = \
{'': ['*']}

install_requires = \
['typing_extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'kink',
    'version': '0.1.0',
    'description': 'Dependency injection for python.',
    'long_description': '# Kink [![Build Status](https://travis-ci.org/kodemore/kink.svg?branch=master)](https://travis-ci.org/kodemore/kink) [![codecov](https://codecov.io/gh/kodemore/kink/branch/master/graph/badge.svg)](https://codecov.io/gh/kodemore/kink)\nDependency injection made for python\n\n## Features\n\n- Easy to use interface\n- Extensible with custom dependency resolvers\n- Automatic dependency injection\n- Lightweight\n- Easy to test\n\n## Installation\n\n```\npip install kink\n```\n\n# Usage\n\n## Simple dependency resolver\n\n```python\nfrom kink import inject\nfrom os import getenv\n\n@inject(dsn=getenv("DB_DSN"), password=getenv("DB_PASSWORD"))\ndef get_database(dsn: str, password: str):\n    ...\n\nconnection = get_database() # Will use `dsn` and `password` from env vars\nconnection_with_custom_dsn = get_database("my_dsn") # Only `password` will be taken from env vars\nconnection_with_custom_password = get_database(password="secret")\n```\n\n### Nested dependencies resolving\n```python\nfrom kink import inject\nfrom os import getenv\n\n@inject(dsn=getenv("DB_DSN"), password=getenv("DB_PASSWORD"))\ndef get_database_settings(dsn: str, password: str):\n    ...\n\n@inject(db_settings=get_database_settings)\ndef get_db_connection(db_settings: dict):\n    ...\n\n# This will create partially injected function\n@inject(db_connection=get_db_connection)\ndef get_user(user_id: int, db_connection) -> dict:\n    ...\n\nget_user(12) # will use injected connection, connection will not be established until `get_user` function is called.\n\nmock_connection = ...\nget_user(12, mock_connection) # you can easily mock connections\n```\n\n### Constructor injection\n```python\nfrom kink import inject\n\ndef get_connection():\n    ...\n\nclass UserRepository:\n    @inject(db_connection=get_connection)\n    def __init__(self, unit_of_work, db_connection):\n        ...\n    \n    def get(self, id: int):\n        ...\n```\n\n## Setting dictionary as a resolver\n\n```python\nfrom kink import inject, set_resolver\n\nset_resolver({\n    "gimme_a": "a",\n    "gimme_b": "b",\n})\n\n@inject()\ndef print_a_b_c(gimme_a: str, gimme_b: str, gimme_c: str):\n    print(gimme_a, gimme_b, gimme_c)\n\n\nprint_a_b_c(gimme_c="c") # will print; a, b, c\n```\n\n## Defining custom dependency resolver\n\nKink supports two types of dependency resolvers:\n- callables which accepts 3 parameters; property name, property type and context\n- classes implementing `kink.resolvers.Resolver` protocol (see `simple_resolver.py` for example implementation)\n\n```python\nfrom kink import inject, set_resolver\nfrom kink.errors import ResolverError\n\n\ndef resolve_dependency_by_type(param_name: str, param_type: type, context):\n    if param_type is str:\n        return "test"\n\n    if param_type is int:\n        return 1\n\n    raise ResolverError()\n\nset_resolver(resolve_dependency_by_type)\n\n@inject()\ndef test_me(one: int, test: str):\n    print(one, test)\n\ntest_me() # will print: 1, "test"\n```\n',
    'author': 'Dawid Kraczkowski',
    'author_email': 'dawid.kraczkowski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kodemore/charmed',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
