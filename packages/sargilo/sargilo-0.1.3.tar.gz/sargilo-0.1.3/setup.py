# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sargilo',
 'sargilo.integrations',
 'sargilo.tests',
 'sargilo.tests.blog',
 'sargilo.tests.blog.migrations',
 'sargilo.tests.blog.south_migrations',
 'sargilo.tests.django111_test_project.django111_test_project',
 'sargilo.tests.django14_test_project.django14_test_project',
 'sargilo.tests.django18_test_project',
 'sargilo.tests.django22_test_project.django22_test_project',
 'sargilo.tests.django30_test_project.django30_test_project']

package_data = \
{'': ['*'],
 'sargilo.tests': ['django111_test_project/*',
                   'django14_test_project/*',
                   'django14_test_project/django14_test_project.egg-info/*',
                   'django22_test_project/*',
                   'django30_test_project/Dockerfile',
                   'django30_test_project/Dockerfile',
                   'django30_test_project/Dockerfile',
                   'django30_test_project/Dockerfile',
                   'django30_test_project/django30_test_project.egg-info/*',
                   'django30_test_project/manage.py',
                   'django30_test_project/manage.py',
                   'django30_test_project/manage.py',
                   'django30_test_project/manage.py',
                   'django30_test_project/poetry.lock',
                   'django30_test_project/poetry.lock',
                   'django30_test_project/poetry.lock',
                   'django30_test_project/poetry.lock',
                   'django30_test_project/pyproject.toml',
                   'django30_test_project/pyproject.toml',
                   'django30_test_project/pyproject.toml',
                   'django30_test_project/pyproject.toml']}

install_requires = \
['ruamel.yaml', 'typing']

setup_kwargs = {
    'name': 'sargilo',
    'version': '0.1.3',
    'description': 'Dynamic loader for test data',
    'long_description': None,
    'author': 'Nick Lehmann',
    'author_email': 'nick@lehmann.sh',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7',
}


setup(**setup_kwargs)
