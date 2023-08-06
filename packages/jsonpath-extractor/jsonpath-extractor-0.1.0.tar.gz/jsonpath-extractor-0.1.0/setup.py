# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonpath']

package_data = \
{'': ['*']}

install_requires = \
['sly>=0.3.0,<0.4.0', 'typing_extensions>=3.7,<4.0']

extras_require = \
{'lint': ['black>=19.3b0,<20.0',
          'flake8>=3.7.8,<4.0.0',
          'isort>=4.3.21,<5.0.0',
          'mypy>=0.750,<0.751',
          'pytest>=5.2.0,<6.0.0',
          'flake8-bugbear>=19.8,<20.0'],
 'test': ['pytest>=5.2.0,<6.0.0', 'pytest-cov>=2.7.1,<3.0.0']}

setup_kwargs = {
    'name': 'jsonpath-extractor',
    'version': '0.1.0',
    'description': 'A selector expression for extracting data from JSON.',
    'long_description': '========\nJSONPATH\n========\n\nA selector expression for extracting data from JSON.\n\nQuickstarts\n<<<<<<<<<<<\n\nInstallation\n~~~~~~~~~~~~\n\nInstall the stable version from PYPI.\n\n.. code-block:: shell\n\n    pip install jsonpath-extractor\n\nOr install the latest version from Github.\n\n.. code-block:: shell\n\n    pip install git+https://github.com/linw1995/jsonpath.git@master\n\n\nUsage\n~~~~~\n\n.. code-block:: python3\n\n    import json\n\n    from jsonpath import parse, Root, Contains, Self\n\n    data = json.loads(\n        """\n        {\n            "goods": [\n                {"price": 100, "category": "Comic book"},\n                {"price": 200, "category": "magazine"},\n                {"price": 200, "no category": ""}\n            ],\n            "targetCategory": "book"\n        }\n    """\n    )\n    expect = [{"price": 100, "category": "Comic book"}]\n\n    assert parse("$.goods[contains(@.category, $.targetCategory)]").find(data) == expect\n\n    assert (\n        Root()\n        .Name("goods")\n        .Array(Contains(Self().Name("category"), Root().Name("targetCategory")))\n        .find(data)\n        == expect\n    )\n',
    'author': '林玮',
    'author_email': 'linw1995@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/linw1995/jsonpath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
