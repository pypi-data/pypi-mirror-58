# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyinsights']

package_data = \
{'': ['*'], 'pyinsights': ['schema/*']}

install_requires = \
['boto3>=1.10.45,<2.0.0', 'jsonschema>=3.2.0,<4.0.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['pyinsights = pyinsights.cli:cli']}

setup_kwargs = {
    'name': 'pyinsights',
    'version': '0.1.1',
    'description': 'AWS CloudWatch Logs Insights is wrapped by Python',
    'long_description': "# PyInsights\n\nA CLI tool To query CloudWatch Logs Insights.\n\n## Usage\n\n### 1. Write Configuration\n\nwrite configuration to `pyinsights.yml` like:\n\n```yaml\nversion: '1.0'\nlog_group_name:\n  - '/ecs/sample'\nquery_string: 'field @message | filter @message like /ERROR/'\nduration: '30m'\nlimit: 10\n```\n\n### 2. Execute command\n\n```bash\npyinsights -c pyinsights.yml -p aws_profile -r region\n```\n",
    'author': 'homoluctus',
    'author_email': 'w.slife18sy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/homoluctus/pyinsights',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
