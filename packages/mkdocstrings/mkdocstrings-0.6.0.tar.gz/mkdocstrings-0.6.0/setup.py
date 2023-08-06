# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mkdocstrings']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mkdocstrings = mkdocstrings.cli:main'],
 'mkdocs.plugins': ['mkdocstrings = mkdocstrings.plugin:MkdocstringsPlugin']}

setup_kwargs = {
    'name': 'mkdocstrings',
    'version': '0.6.0',
    'description': 'Automatic documentation from docstrings, for mkdocs.',
    'long_description': '# mkdocstrings\n[![pipeline status](https://gitlab.com/pawamoy/mkdocstrings/badges/master/pipeline.svg)](https://gitlab.com/pawamoy/mkdocstrings/pipelines)\n[![coverage report](https://gitlab.com/pawamoy/mkdocstrings/badges/master/coverage.svg)](https://gitlab.com/pawamoy/mkdocstrings/commits/master)\n[![documentation](https://img.shields.io/badge/docs-latest-green.svg?style=flat)](https://pawamoy.github.io/mkdocstrings)\n[![pypi version](https://img.shields.io/pypi/v/mkdocstrings.svg)](https://pypi.org/project/mkdocstrings/)\n\nAutomatic documentation from docstrings, for mkdocs.\n\nThis plugin is still in alpha status. Here is how it looks with the [mkdocs-material theme](https://squidfunk.github.io/mkdocs-material/) for now:\n\n![mkdocstrings](https://user-images.githubusercontent.com/3999221/71327911-e467d000-250e-11ea-83e7-a81ec59f41e2.gif)\n\n## Features\n- **Works great with Material theme:** `mkdocstrings` was designed to work best with\n  the great [Material theme](https://squidfunk.github.io/mkdocs-material/).\n- **Support for type annotations:** `mkdocstrings` uses your type annotations to display parameters types\n  or return types.\n- **Recursive documentation of Python objects:** just write the module dotted-path, and you get the full module docs.\n  No need to ask for each class, function, etc.\n- **Support for documented attribute:** attributes (variables) followed by a docstring (triple-quoted string) will\n  be recognized by `mkdocstrings`, in modules, classes and even in `__init__` methods.\n- **Support for objects properties:** `mkdocstrings` will know if a method is a `staticmethod`, a `classmethod` or else,\n  it will also know if a property is read-only or writable, and more! These properties will be displayed\n  next to the object signature.\n- **Every object has a TOC entry and a unique permalink:** the navigation is greatly improved! Click the anchor\n  next to the object signature to get its permalink, which is its Python dotted-path.\n- **Auto-reference other objects:** `mkdocstrings` makes it possible to reference other Python objects from your\n  markdown files, and even from your docstrings, with the classic Markdown syntax:\n  `[this object][package.module.object]` or directly with `[package.module.object][]`.\n- **Google-style sections support in docstrings:** `mkdocstrings` understands `Arguments:`, `Raises:`\n  and `Returns:` sections. It will even keep the section order in the generated docs.\n- **Support for source code display:** `mkdocstrings` can add a collapsible div containing the source code of the\n  Python object, directly below its signature, with the right line numbers.\n- **Admonition support in docstrings:** blocks like `Note: ` or `Warning: ` will be transformed\n  to their [admonition](https://squidfunk.github.io/mkdocs-material/extensions/admonition/) equivalent.\n  *We do not support nested admonitions in docstrings!*\n- **Sane defaults:** you should be able to just drop the plugin in your configuration and enjoy your auto-generated docs.\n- **Configurable:** *(soon)* `mkdocstrings` is configurable globally, and per autodoc instruction.\n\nTo get an example of what is possible, check `mkdocstrings`\'\nown [documentation](https://pawamoy.github.io/mkdocstrings), generated with itself.\n\n## Requirements\nmkdocstrings requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.8\n\n# make it available globally\npyenv global system 3.6.8\n```\n</details>\n\n## Installation\nWith `pip`:\n```bash\npython3.6 -m pip install mkdocstrings\n```\n\n## Usage\n\n```yaml\n# mkdocs.yml\n\n# designed to work best with material theme\ntheme:\n  name: "material"\n\n# these extensions are required for best results\nmarkdown_extensions:\n  - admonition\n  - codehilite\n  - attr_list\n  - pymdownx.details\n  - pymdownx.superfences\n  - pymdownx.inlinehilite\n  - toc:\n      permalink: true\n\nplugins:\n  - search\n  - mkdocstrings\n```\n\nIn one of your markdown files:\n\n```markdown\n# Reference\n\n::: my_library.my_module.my_class\n```\n\nYou can reference objects from other modules in your docstrings:\n\n```python\ndef some_function():\n    """\n    This is my function.\n\n    It references [another function][package.submodule.function].\n    It also references another object directly: [package.submodule.SuperClass][].\n    """\n    pass\n```\n\nAdd some style in `docs/custom.css`:\n\n```css\ndiv.autodoc {\n  padding-left: 25px;\n  border-left: 4px solid rgba(230, 230, 230);\n}\n```\n\nAnd add it to your configuration:\n\n```yaml\nextra_css:\n  - custom.css\n```\n',
    'author': 'Timothée Mazzucotelli',
    'author_email': 'pawamoy@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/pawamoy/mkdocstrings',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
