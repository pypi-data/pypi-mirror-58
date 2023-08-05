# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.series']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-series-plugin',
    'version': '1.0.2',
    'description': 'An installable version of the original Pelican Series plugin',
    'long_description': '# Pelican Series: A Plugin for Pelican\n\nThis plugin extends the original series plugin by [FELD Boris <lothiraldan@gmail.com>](https://github.com/Lothiraldan)\nCopyright (c) [Leonardo Giordani <giordani.leonardo@gmail.com>](https://github.com/TheDigitalCatOnline)\nThis plugin is also in the [Pelican Plugins repository](https://github.com/getpelican/pelican-plugins)\n\nThe series plugin allows you to join different posts into a series.\n\nIn order to mark posts as part of a series, use the `:series:` metadata:\n\n    :series:  NAME_OF_THIS_SERIES\n\nor, in Markdown syntax\n\n    Series: NAME_OF_THIS_SERIES\n\nThe plugin collects all articles belonging to the same series and provides\nseries-related variables that you can use in your template.\n\n## Indexing\n\nBy default articles in a series are ordered by date and then automatically numbered.\n\nIf you want to force a given order just specify the `:series_index:` metadata or in Markdown `series_index:`,\nstarting from 1. All articles with this enforced index are put at the beginning of\nthe series and ordered according to the index itself. All the remaining articles\ncome after them, ordered by date.\n\nThe plugin provides the following variables to your templates\n\n    * `article.series.name` is the name of the series as specified in the article metadata\n    * `article.series.index` is the index of the current article inside the series\n    * `article.series.all` is an ordered list of all articles in the series (including the current one)\n    * `article.series.all_previous` is an ordered list of the articles published before the current one\n    * `article.series.all_next` is an ordered list of the articles published after the current one\n    * `article.series.previous` is the previous article in the series (a shortcut to `article.series.all_previous[-1]`)\n    * `article.series.next` is the next article in the series (a shortcut to `article.series.all_next[0]`)\n\nFor example:\n\n    {% if article.series %}\n        <p>This post is part {{ article.series.index }} of the "{{ article.series.name }}" series:</p>\n        <ol class="parts">\n            {% for part_article in article.series.all %}\n                <li {% if part_article == article %}class="active"{% endif %}>\n                    <a href=\'{{ SITEURL }}/{{ part_article.url }}\'>{{ part_article.title }}</a>\n                </li>\n            {% endfor %}\n        </ol>\n    {% endif %}\n\n\nJoins articles in a series and provides variables to manage the series in the template.\n\n## Installation\n\nThis plugin can be installed via:\n\n    pip install pelican-series-plugin\n    \nNext add it to the `PLUGINS` section in `pelicanconf.py`\n\n```python\nPLUGINS = [\n    \'...\',\n    \'pelican.plugins.series\',\n    \'...\'\n]\n```\n\n## Contributing\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/johanvergeer/pelican-series/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pelican-series-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
