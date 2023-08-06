# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.pelican_cite']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0',
 'pybtex-author-year-label>=0.1.0,<0.2.0',
 'pybtex>=0.22.2,<0.23.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-cite',
    'version': '0.1.1',
    'description': 'Allows the use of BibTeX citations within a Pelican site',
    'long_description': 'pelican-cite\n==============\n\nAllows the use of BibTeX citations within a Pelican site.\n\nHow to Use\n==========\n\nThis plugin reads a user-specified BibTeX file and generates bibliographic\ninformation within your articles and pages.\n\nConfiguration is simply:\n\n```python\nPUBLICATIONS_SRC = \'content/pubs.bib\'\n```\n\nIf the file is present and readable, then content will be scanned for references\nto citation keys. These take the format `[@Bai2011]` or `[@@Bai2011]`. These\nwill be replaced by incline citations which provide links to the full\nbibliographic information at the end of the article. The former reference would\nbe replaced by a citation of the form "Bai & Stone (2011)", while the latter\nwould be replaced by "(Bai & Stone, 2011)".\n\nIf a citation key is used which does not exist within the BibTeX file then\na warning will be displayed.\n\nThe BibTeX file may, optionally, be provided or overridden on a per-article\nbasis by supplying the meta-data `publications_src`.\n\nAttribution\n===========\n`pelican-cite` is based on the\n[pelican-bibtex](https://github.com/vene/pelican-bibtex) plugin written by\n[Vlad Niculae](https://github.com/vene)\nand [pelican-cite](https://github.com/cmacmackin/pelican-cite) written by\n[Chris MacMackin](https://github.com/cmacmackin).\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pelican-cite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
