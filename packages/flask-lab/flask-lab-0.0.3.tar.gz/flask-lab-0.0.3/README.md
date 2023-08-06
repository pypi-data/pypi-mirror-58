# Flask-Lab

Flask-Lab can create a restful api directly from database schema without any coding.

Flask-Lab is built with flask and peewee.

## Quick Start

### Install

```
pip install flask-lab
```

or even better, with `poetry`:

```
poetry add flask-lab
```

This will install the `flask_lab` module and a `flask-lab` command.

### Create a demo sqlite database(optional)

If you don't have any database to connect and just want to try out flask-lab,
you could create a demo database with a user and an article table for show-case:

```
flask-lab --create-demo
```

This will create a `flask_lab_demo.db` file with some fake data.

### Start the flask-lab restful service

```
flask-lab --engine sqlite --database flask_lab_demo.db
```

Then open your browser at http://localhost:5000/api/user or http://localhost:5000/api/article and you can see a list of users or articles.

This will also create `flask_lab_models.py` and `flask_lab_app.py`, which you could use to build your app.

## Docs

```
flask-lab -h

Usage: flask_lab.py [options], flask_lab.py -h for detailed help

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST
  -p PORT, --port=PORT
  -u USER, --user=USER
  -P, --password
  -e ENGINE, --engine=ENGINE
                        Database type, e.g. sqlite, mysql, postgresql or
                        cockroachdb. Default is "postgresql".
  -s SCHEMA, --schema=SCHEMA
  -t TABLES, --tables=TABLES
                        Only generate the specified tables. Multiple table
                        names should be separated by commas.
  -v, --views           Generate model classes for VIEWs in addition to
                        tables.
  -i, --info            Add database information and other metadata to top of
                        the generated file.
  -o, --preserve-order  Model definition column ordering matches source table.
  -I, --ignore-unknown  Ignore fields whose type cannot be determined.
  -L, --legacy-naming   Use legacy table- and column-name generation.
  -m MODEL_FILE, --model-file=MODEL_FILE
                        Model filename to generate
  -a APP_FILE, --app-file=APP_FILE
                        Flask App filename to generate
  -l LISTEN_ADDRESS, --listen-address=LISTEN_ADDRESS
                        Port for flask app to listen on. Format: 0.0.0.0:5000
  -C, --create-demo     Create a demo database with Article and User Model to
                        demo Flask-Lab
  -d DATABASE, --database=DATABASE
                        Database to use
```

detailed docs coming soon...


## TODO

- filter_x methods
- include and exclude
- date_format
- user, group and permission tables like django-admin
- a react-admin based admin panel like django-admin
- OpenAPI documentation
