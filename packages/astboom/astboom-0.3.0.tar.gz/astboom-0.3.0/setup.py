# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astboom', 'astboom.visualizers']

package_data = \
{'': ['*']}

install_requires = \
['asciitree>=0.3.3,<0.4.0', 'click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['astboom = astboom.main:cli']}

setup_kwargs = {
    'name': 'astboom',
    'version': '0.3.0',
    'description': 'Visualize Python AST in console.',
    'long_description': "# astboom\n![PyPI](https://img.shields.io/pypi/v/astboom) \n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/astboom)\n![GitHub](https://img.shields.io/github/license/lensvol/astboom)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nVisualize Python AST/CST/ST in console using ASCII graphics.\n\nAST is displayed as provided by standard `ast` module, CST is displayed as provided by `lib2to3`.\n\n## Example\n\n![Example usage](https://raw.githubusercontent.com/lensvol/astboom/master/docs/example.png)\n\n## Usage\n\nSimply provide a valid Python source code string as an argument\nand a corresponding AST/CST/ST will be displayed.\n\n```\nUsage: astboom ast [OPTIONS] [SOURCE]\n\n  Display Abstract Syntax Tree for a given source.\n\nOptions:\n  --no-pos      Hide 'col_offset' and 'lineno' fields.\n  --hide-empty  Hide empty fields.\n  --help        Show this message and exit.\n```\n\n```\nUsage: astboom cst [OPTIONS] [SOURCE]\n\n  Display Concrete Source Tree for a given source.\n\nOptions:\n  --help  Show this message and exit.\n```\n\n```\nUsage: astboom st [OPTIONS] [SOURCE]\n\n  Display parse tree for a given source.\n\nOptions:\n  --help  Show this message and exit.\n```\n\nIf no source provided as an argument, then tool will attempt to read it\nfrom *STDIN*.\n\n## Installation\n\n```shell script\n# pip install astboom\n```\n\n## Getting started with development\n\n```shell script\n# git clone https://github.com/lensvol/astboom\n# poetry install --develop\n```\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n\n## Authors\n\n* **Kirill Borisov** ([lensvol@gmail.com](mailto:lensvol@gmail.com))\n",
    'author': 'Kirill Borisov',
    'author_email': 'lensvol@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lensvol/astboom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
