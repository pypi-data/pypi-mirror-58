# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aioaerospike', 'aioaerospike.protocol']

package_data = \
{'': ['*']}

install_requires = \
['bcrypt>=3.1,<4.0', 'construct>=2.9,<3.0', 'msgpack>=0.6.2,<0.7.0']

setup_kwargs = {
    'name': 'aioaerospike',
    'version': '0.1.5',
    'description': 'Async Pure Python implementation of Aerospike client',
    'long_description': "# aioaerospike\n[![codecov](https://codecov.io/gh/aviramha/aioaerospike/branch/master/graph/badge.svg)](https://codecov.io/gh/aviramha/aioaerospike)\n[![Build Status](https://travis-ci.com/aviramha/aioaerospike.svg?branch=master)](https://travis-ci.com/aviramha/aioaerospike)\n\nThis library is planned to be an async API for Aerospike.\nThe library will be Pure-Python, Protocol based on the C Client.\n\n## Installation\nUsing pip\n```\n$ pip install aioaerospike\n```\n\n## Contributing\n\nTo work on the `aioaerospike` codebase, you'll want to fork the project and clone it locally and install the required dependencies via [poetry](https://poetry.eustace.io):\n\n```sh\n$ git clone git@github.com:{USER}/aioaerospike.git\n$ make install\n```\n\nTo run tests and linters use command below (Requires aerospike to run locally on port 3000):\n\n```sh\n$ make lint && make test\n```\n\nIf you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:\n\n```sh\n$ make lint-black\n```\n\n## License\n\n`aioaerospike` is licensed under the MIT license. See the license file for details.\n\n# Latest changes\n\n## 0.1.6 (XXXX-XX-XX)\n\n## 0.1.5 (2019-12-17)\n- Added TTL argument for put_key\n- Added operate method, enables users to interact with lower-level API to do specific actions, such as multi op\n  (read, write, modify, etc) in same message.\n- Added UNDEF/AerospikeNone for the option of empty bins, when reading specific bins.\n\n## 0.1.4 (2019-12-07)\n- Added delete key method\n- Added key_exists method\n- Changed signature of put_key to be a dict, for easy multiple bins insert.\n\n## 0.1.3 (2019-12-07)\n- Changed all enums to uppercase\n- Added tests for all supported key types\n- Added support for dict and list as values.\n\n## 0.1.2 (2019-12-07)\n- Fixed key digest, key type can be all supported types (int, float, str, bytes)\n\n## 0.1.1 (2019-12-07)\n- Fixed license and metadata\n\n\n## This package is 3rd party, unrelated to Aerospike company\n",
    'author': 'Aviram Hassan',
    'author_email': 'aviramyhassan@gmail.com',
    'url': 'https://github.com/aviramha/aioaerospike',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
