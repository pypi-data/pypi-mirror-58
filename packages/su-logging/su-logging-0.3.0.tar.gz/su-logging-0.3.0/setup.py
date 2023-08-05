# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['su', 'su.logging']

package_data = \
{'': ['*']}

extras_require = \
{'structured': ['logstash_formatter>=0.5.17,<0.6.0']}

setup_kwargs = {
    'name': 'su-logging',
    'version': '0.3.0',
    'description': 'Logging for Stockholm University',
    'long_description': '# Logging for Stockholm University\n\nEasy to use logging for Stockholm University.\n\n## Usage\n\n```python\nfrom su.logging import logging\n\nlogger = logging.getLogger("myapp")\nlogger.info("My INFO message")\n```\n\nFor easier developing you can also enable console logging:\n```python\nfrom su.logging import console, logging\n\nlogger = logging.getLogger("myapp")\nlogger.info("My INFO message")\n```\n\n### Structured logging\nWe use\n[logstash_formatter](https://github.com/ulule/python-logstash-formatter/)\'s\n`LogstashFormatterV1` and remove some unused/unnecesary fields.\n\nDepend on `su-logging[structured]` in e.g. your `requirements.txt` and then:\n```python\nfrom su.logging import structured, logging\n\nlogger = logging.getLogger("myapp")\nlogger.info("User logged in", extra={"user": "simlu"})\n\ntry:\n    raise Exception("User performed illegal activity")\nexcept Exception as e:\n    logger.exception(e, extra={"user": "simlu"})\n```\n\n## TODO\n* [ ] [Some sort of versioning?](https://github.com/sdispater/poetry/issues/1036#issuecomment-489880822)\n',
    'author': 'Simon Lundström',
    'author_email': 'simlu+github@su.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stockholmuniversity/su-logging',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
