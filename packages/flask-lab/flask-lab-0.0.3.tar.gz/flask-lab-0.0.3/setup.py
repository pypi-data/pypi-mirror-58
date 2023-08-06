# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flask_lab']
install_requires = \
['flask>=1.1.1,<2.0.0', 'peewee>=3.13,<4.0']

entry_points = \
{'console_scripts': ['flask-lab = flask_lab:main']}

setup_kwargs = {
    'name': 'flask-lab',
    'version': '0.0.3',
    'description': 'Django-admin for flask with restful API.',
    'long_description': '# Flask-Lab\n\nFlask-Lab can create a restful api directly from database schema without any coding.\n\nFlask-Lab is built with flask and peewee.\n\n## Quick Start\n\n### Install\n\n```\npip install flask-lab\n```\n\nor even better, with `poetry`:\n\n```\npoetry add flask-lab\n```\n\nThis will install the `flask_lab` module and a `flask-lab` command.\n\n### Create a demo sqlite database(optional)\n\nIf you don\'t have any database to connect and just want to try out flask-lab,\nyou could create a demo database with a user and an article table for show-case:\n\n```\nflask-lab --create-demo\n```\n\nThis will create a `flask_lab_demo.db` file with some fake data.\n\n### Start the flask-lab restful service\n\n```\nflask-lab --engine sqlite --database flask_lab_demo.db\n```\n\nThen open your browser at http://localhost:5000/api/user or http://localhost:5000/api/article and you can see a list of users or articles.\n\nThis will also create `flask_lab_models.py` and `flask_lab_app.py`, which you could use to build your app.\n\n## Docs\n\n```\nflask-lab -h\n\nUsage: flask_lab.py [options], flask_lab.py -h for detailed help\n\nOptions:\n  -h, --help            show this help message and exit\n  -H HOST, --host=HOST\n  -p PORT, --port=PORT\n  -u USER, --user=USER\n  -P, --password\n  -e ENGINE, --engine=ENGINE\n                        Database type, e.g. sqlite, mysql, postgresql or\n                        cockroachdb. Default is "postgresql".\n  -s SCHEMA, --schema=SCHEMA\n  -t TABLES, --tables=TABLES\n                        Only generate the specified tables. Multiple table\n                        names should be separated by commas.\n  -v, --views           Generate model classes for VIEWs in addition to\n                        tables.\n  -i, --info            Add database information and other metadata to top of\n                        the generated file.\n  -o, --preserve-order  Model definition column ordering matches source table.\n  -I, --ignore-unknown  Ignore fields whose type cannot be determined.\n  -L, --legacy-naming   Use legacy table- and column-name generation.\n  -m MODEL_FILE, --model-file=MODEL_FILE\n                        Model filename to generate\n  -a APP_FILE, --app-file=APP_FILE\n                        Flask App filename to generate\n  -l LISTEN_ADDRESS, --listen-address=LISTEN_ADDRESS\n                        Port for flask app to listen on. Format: 0.0.0.0:5000\n  -C, --create-demo     Create a demo database with Article and User Model to\n                        demo Flask-Lab\n  -d DATABASE, --database=DATABASE\n                        Database to use\n```\n\ndetailed docs coming soon...\n\n\n## TODO\n\n- filter_x methods\n- include and exclude\n- date_format\n- user, group and permission tables like django-admin\n- a react-admin based admin panel like django-admin\n- OpenAPI documentation\n',
    'author': 'Yifei Kong',
    'author_email': 'kongyifei@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yifeikong/flask-lab',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
