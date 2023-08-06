# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['iscc']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=6,<7', 'xxhash>=1,<2']

setup_kwargs = {
    'name': 'iscc',
    'version': '1.0.5',
    'description': 'ISCC: Reference Implementation',
    'long_description': "# ISCC - Spec and Reference Code\n\n[![Build](https://travis-ci.org/iscc/iscc-specs.svg?branch=master)](https://travis-ci.org/iscc/iscc-specs)\n[![Version](https://img.shields.io/pypi/v/iscc.svg)](https://pypi.python.org/pypi/iscc/)\n[![License](https://img.shields.io/pypi/l/iscc.svg)](https://pypi.python.org/pypi/iscc/)\n[![Downloads](https://pepy.tech/badge/iscc)](https://pepi.tech/project/iscc)\n\nThe **International Standard Content Code** is a proposal for an [open standard](https://en.wikipedia.org/wiki/Open_standard) for decentralized content identification. This repository contains the specification of the proposed **ISCC Standard** and a reference implementation in Python3. The latest published version of the specification can be found at [iscc.codes](https://iscc.codes)\n\n| NOTE: This is a low level reference implementation. For easy generation of ISCC codes see: [iscc-cli](https://github.com/iscc/iscc-cli) |\n| --- |\n\n## Installing the reference code\n\nThe reference code is published with the package name [iscc](https://pypi.python.org/pypi/iscc) on Python Package Index. Install it with:\n\n``` bash\npip install iscc\n```\n\n## Using the reference code\n\nA short example on how to create an ISCC Code with the reference implementation.\n\n``` python\nimport iscc\n\n# Generate ISCC Component Codes\nmid, title, extra = iscc.meta_id('Title of Content')\ncid = iscc.content_id_text('some text')\ndid = iscc.data_id('path/to/mediafile.doc')\niid, tophash = iscc.instance_id('path/to/mediafile.doc')\n\n# Join ISCC Components to fully qualified ISCC Code\niscc_code = '-'.join([mid, cid, did, iid])\nprint('ISCC:{}'.format(iscc_code))\n```\n\n## Working with the specification\n\nThe entire **ISCC Specification** is written in plain text [Markdown](https://en.wikipedia.org/wiki/Markdown). The markdown content is than built and published with the excellent [mkdocs](http://www.mkdocs.org/) documetation tool. If you have some basic command line skills you can build and run the specification site on your own computer. Make sure you have the [git](https://git-scm.com/) and [Python](https://www.python.org/) installed on your system and follow these steps on the command line:\n\n``` bash\ngit clone https://github.com/iscc/iscc-specs.git\ncd iscc-specs\npip install -r requirements.txt\nmkdocs serve\n```\n\nAll specification documents can be found in the `./docs` subfolder or the repository. The recommended editor for the markdown files is [Typora](https://typora.io/). If you have commit rights to the [main repository](https://github.com/iscc/iscc-specs) you can deploy the site with a simple `mkdocs gh-deploy`.\n\n## Contribute\n\nPull requests and other contributions are welcome. Use the [Github Issues](https://github.com/iscc/iscc-specs/issues) section of this project to discuss ideas for the **ISCC Specification**. You may also want  join our developer chat on Telegram at <https://t.me/iscc_dev>.\n\n## License\n\nAll of documentation is licensed under the [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).\n\nReference code is licensed under BSD-2-Clause.\n",
    'author': 'Titusz Pan',
    'author_email': 'tp@py7.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://iscc.codes/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
