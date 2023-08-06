# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.timegraphics']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-timegraphics-plugin',
    'version': '1.0.1',
    'description': 'Easily embed Time.Graphics timelines in your Pelican articles',
    'long_description': '# Time.Graphics plugin for Pelican: A Plugin for Pelican\n\nEasily embed Time.Graphics timelines in your Pelican articles\n\n## Installation\n\nThis plugin can be installed via:\n\n    pip install pelican-timegraphics-plugin\n    \nNext add it to the `PLUGINS` section of `pelicanconf.py`.\n\n```python\nPLUGINS = [\n    \'...\',\n    \'pelican.plugins.timegraphics\'\n    \'...\',\n]\n```\n    \n## Usage\n\nIn your articles, just add lines to your posts that look like:\n\n```markdown\n[timegraphics:id=123456,width=100%,height=400,allowfullscreen=1,frameborder=0]\n```\n\nThe resulting html will look like\n\n```html\n<iframe src="https://time.graphics/embed?v=1&id=123456" width="100%" height="400" frameborder="0" allowfullscreen></iframe>\n<a style="font-size: 12px; text-decoration: none;" title="Powered by Time.Graphics" href="https://time.graphics">Powered by Time.Graphics</a></div>\n```\n\n### Settings\n\n#### `TIMEGRAPHICS_DEFAULT_WIDTH`\n\nThe default with of a timeline. Default is `\'100%\'`\n- Can be overruled on each timeline with the `width` parameter\n\n#### `TIMEGRAPHICS_DEFAULT_HEIGHT`\n\n- The default height of a timeline. Default is `\'400\'`\n- Can be overruled on each timeline with the `height` parameter\n\n#### `TIMEGRAPHICS_ALLOW_FULLSCREEN`\n\n- Sets the default on whether users of your site can view timelines in fullscreen.\n- Allowed values are `\'0\'` and `\'1\'`\n- Default is `\'1\'`\n- Can be overruled on each timeline with the `allowfullscreen` parameter\n\n#### `TIMEGRAPHICS_SHOW_FRAMEBORDER`\n\n- Whether to show a border around each timeline\n- Allowed values are `\'0\'` and `\'1\'`\n- Default is `\'0\'`\n- Can be overruled on each timeline with the `frameborder` parameter\n\n#### `TIMEGRAPHICS_SHOW_POWERED_BY`\n\n- Whether to show "Powered by Time.Graphics" under the timeline\n- Allowed values are `True` and `False`\n- Default is `True` \n\n## Contributing\n\nContributions are welcome and much appreciated. Every little bit helps. \nYou can contribute by improving the documentation, adding missing features, and fixing bugs.\nYou can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, \nbeginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/johanvergeer/pelican-timegraphics-plugin/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pelican-timegraphics-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
