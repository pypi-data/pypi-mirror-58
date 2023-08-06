#!/usr/bin/env python3

"""
Flask-Lab - Django-admin for flask with restful API.
"""

import inspect
import json
import os
import re
import sys
from functools import wraps
from typing import Iterable

from flask import current_app, jsonify, request
from flask.views import MethodView
from peewee import Model
from playhouse.shortcuts import model_to_dict
from pwiz import get_connect_kwargs, get_option_parser

"""
Default config
"""

FLASK_LAB_ITEM_PER_PAGE = 20
FLASK_LAB_PAGE_PARAM_NAME = "_page"
FLASK_LAB_SORT_PARAM_NAME = "_sort"
FLASK_LAB_PAGE_SIZE_PARAM_NAME = "_page_size"
FLASK_LAB_OFFSET_PARAM_NAME = "_offset"
FLASK_LAB_LIMIT_PARAM_NAME = "_limit"
FLASK_LAB_FIELDS_PARAM_NAME = "_fields"

FLASK_LAB_PAGE_SIZE = 20  # default results per page
FLASK_LAB_BATCH_SIZE = 100  # default bulk create batch size


"""
Utility funcitons
"""


def compact(iterable: Iterable):
    """
    删除数组中为falsy、0的元素
    >>> list(compact([0, 1, 2]))
    [1, 2]
    >>> list(compact([1, 2]))
    [1, 2]
    >>> list(compact([0, 1, False, 2, '', 3]))
    [1, 2, 3]
    """
    for el in iterable:
        if el:
            yield el


def ensure_str(s, encoding="utf-8", errors="ignore"):
    """
    >>> ensure_str(b'hello') == 'hello'
    True
    >>> ensure_str('你好') == '你好'
    True
    >>> isinstance(ensure_str('你好'), str)
    True
    """

    if isinstance(s, bytes):
        return s.decode(encoding=encoding, errors=errors)
    if isinstance(s, (int, float)):
        return str(s)
    if isinstance(s, (dict, list)):
        return json.dumps(s)
    if s is None:
        return ""
    return s


def snake_case(s):
    """
    convert token(s) to snake case
    >>> snake_case('fooBar')
    'foo_bar'
    >>> snake_case('foo_bar')
    'foo_bar'
    >>> snake_case('foo-bar')
    'foo_bar'
    >>> snake_case('FooBar')
    'foo_bar'
    >>> snake_case('Foo-Bar')
    'foo_bar'
    >>> snake_case('foo bar')
    'foo_bar'
    """
    s = ensure_str(s)
    # turing uppercase to seperator with lowercase
    s = re.sub(r"[A-Z]", r"-\g<0>", s, flags=re.UNICODE)
    words = compact(re.split(r"\W+", s, flags=re.UNICODE))
    return "_".join([word.lower() for word in words])


def dash_case(s):
    """
    >>> dash_case('fooBar')
    'foo-bar'
    >>> dash_case('foo_bar')
    'foo-bar'
    >>> dash_case('foo-bar')
    'foo-bar'
    >>> dash_case('FooBar')
    'foo-bar'
    >>> dash_case('Foo-Bar')
    'foo-bar'
    >>> dash_case('foo bar')
    'foo-bar'
    """
    if s:
        s = snake_case(s).replace("_", "-")
    return s


slugify = dash_case

"""
Restful methods
"""


class MetaEndpoint(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        filters = {}
        for k, v in attrs.items():
            if (
                inspect.isfunction(v)
                and k.startswith("get_")
                and k not in ("get_many", "get_one")
            ):
                fields[k[4:]] = v
            if inspect.isfunction(v) and k.startswith("filter_"):
                fields[k[7:]] = v
        for base in bases:
            if hasattr(base, "_fields"):
                fields.update(base._fields)
            if hasattr(base, "_filters"):
                filters.update(base._filters)

        attrs["_fields"] = fields
        attrs["_filters"] = filters

        return type.__new__(cls, name, bases, attrs)


def catch_exception(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as ex:
            if current_app.debug:
                raise
            return (
                jsonify(
                    {"status": "failed", "errmsg": str(ex), "data": [], "count": 0}
                ),
                400,
            )

    return wrapped


class Endpoint(metaclass=MetaEndpoint):

    model: Model = None
    timefmt: str = None
    empty_value_display: str = None
    null_value_display: str = None
    fields: tuple = tuple()
    exclude: tuple = tuple()

    def queryset(self):
        return self.model.select()

    def get_many(self):
        """
        1. 支持 django rest framework 的查询语法
        2. 支持使用 limit/offset or page/page_size 方式分页
        3. 支持使用 fields 字段限制返回字段
        4. 使用 sort 指定排序方式
        """
        args = request.args.to_dict()

        page = args.pop(FLASK_LAB_PAGE_PARAM_NAME, None)
        page_size = args.pop(FLASK_LAB_PAGE_SIZE_PARAM_NAME, None)
        offset = args.pop(FLASK_LAB_OFFSET_PARAM_NAME, 0)
        limit = args.pop(FLASK_LAB_LIMIT_PARAM_NAME, None)
        sort = args.pop(FLASK_LAB_SORT_PARAM_NAME, None)
        fields = args.pop(FLASK_LAB_FIELDS_PARAM_NAME, None)

        query = self.queryset()
        if args:
            query = query.filter(**args)
        # limit fields to return
        if fields:
            fields = fields.split(",")
            select_fields = []
            for field in fields:
                select_field = getattr(self.model, field, None)
                if select_field:
                    select_fields.append(select_field)
            query = query.select(*select_fields)

        # parsing page and page_size
        if page:
            page = int(page)
        else:
            page = 1

        if page_size:
            page_size = int(page_size)
        else:
            page_size = FLASK_LAB_PAGE_SIZE

        if limit:
            limit = int(limit)
        else:
            limit = FLASK_LAB_PAGE_SIZE

        if page and page_size:
            query = query.paginate(page, page_size)
        elif limit:
            query = query.offset(offset).limit(limit)

        # change returning sort
        if sort:
            if sort[0] == "-":
                order_column, direction = sort[1:], "DESC"
            else:
                order_column, direction = sort, "ASC"
            field = getattr(self.model, order_column)
            if direction == "DESC":
                field = field.desc()
            query = query.order_by(field)

        data = []
        for obj in query:
            obj_dict = model_to_dict(obj, recurse=False)
            obj_dict = self._add_extra_fields(obj_dict, obj.id)
            data.append(obj_dict)
        count = query.count()
        return data, count

    def get_one(self, pk):
        obj = self.model.get_by_id(pk)
        obj_dict = model_to_dict(obj, recurse=False)
        obj_dict = self._add_extra_fields(obj_dict, obj.id)
        return obj_dict

    def post_many(self, obj_dicts):
        objs = []
        for obj_dict in obj_dicts:
            objs.append(self.model(**obj_dict))
        self.model.bulk_create(objs, batch_size=FLASK_LAB_BATCH_SIZE)
        data = []
        for obj in objs:
            data.append(model_to_dict(obj, recurse=True))
        return data

    def post_one(self, obj_dict):
        obj = self.model.create(**obj_dict)
        return model_to_dict(obj, recurse=True)

    def put_many(self, obj_dicts):
        raise NotImplementedError("Bulk update is not supported for now.")

    def put_one(self, pk, obj_dict):
        self.model.update(**obj_dict).where(self.model.id == pk)
        obj_dict = model_to_dict(obj, recurse=True)
        obj_dict = self._add_extra_fields(obj_dict, obj.id)

    def delete_one(self, pk):
        self.model.delete_by_id(pk)

    def _add_extra_fields(self, result, pk):
        for field, method in self._fields.items():
            result[field] = method(self, pk)
        return result

    @catch_exception
    def do_get(self, pk=None):
        if pk is None:
            data, count = self.get_many()
        else:
            # Always return an array, which is easy for static languages like go to parse.
            data = [self.get_one()]
            count = 1
        if data is None:
            return (
                jsonify(
                    {"status": "failed", "errmsg": "Not Found", "data": [], "count": 0}
                ),
                404,
            )
        return (
            jsonify({"data": data, "count": count, "status": "ok", "errmsg": ""}),
            200,
        )

    @catch_exception
    def do_post(self):
        args = request.get_json()
        if isinstance(args, list):
            data = self.post_many(args)
        else:
            data = [self.post_one(args)]  # Always return an array, see above comments
        return (
            jsonify({"status": "ok", "errmsg": "", "data": data, "count": len(data)}),
            200,
        )

    @catch_exception
    def do_put(self, pk=None):
        args = request.get_json()
        if isinstance(args, list):
            data = self.put_many(args)
        else:
            assert pk == args["id"]
            data = self.put_one(pk, args)
        return (
            jsonify({"status": "ok", "errmsg": "", "data": data, "count": len(data)}),
            201,
        )

    @catch_exception
    def do_delete(self, pk):
        self.delete_one(pk)
        return jsonify({"status": "ok", "errmsg": "", "data": [], "count": 0}), 204

    def as_views(self):
        # Proxy methods
        def get(_self, pk=None):
            return self.do_get(pk)

        def post(_self):
            return self.do_post()

        def put(_self, pk=None):
            return self.put(pk)

        def delete(_self, pk):
            return self.delete(pk)

        if not hasattr(self, "model"):
            raise ValueError(
                "No 'model' attribute found for Endpoint: %s" % self.__class__.__name__
            )
        # Dynamically craete a Flask MethodView for api
        ModelView = type(
            self.model.__name__ + "MethodView",
            (MethodView,),
            dict(get=get, post=post, put=put, delete=delete),
        )
        views = ModelView.as_view(self.model.__name__ + "Api")
        return views

    @classmethod
    def name(cls):
        return cls.model.__name__


def ensure_endpoint(model):
    if issubclass(model, Endpoint):
        return model
    return type(model.__name__ + "Endpoint", (Endpoint,), dict(model=model))


def put(self, pk):
    try:
        args = request.get_json()
        obj = self.model.get_or_none(id=pk)
        if obj is None:
            obj.create(**args)
            return (
                jsonify({"status": "ok", "errmsg": "", "data": model_to_dict(obj)}),
                201,
            )
        else:
            obj.update(**args)
            return jsonify({"status": "ok", "errmsg": "", "data": model_to_dict(obj)})
    except Exception as ex:
        if current_app.debug:
            raise
        return jsonify({"status": "failed", "errmsg": str(ex), "data": None}), 400


class FlaskLab:
    def init_app(self, app, endpoints, url_prefix="/api"):
        """
        Call FlaskLab.init_app(app, [YourModel, AnotherModel]) to setup the views
        """
        default_config = dict(
            FLASK_LAB_PAGE_PARAM_NAME=FLASK_LAB_PAGE_PARAM_NAME,
            FLASK_LAB_SORT_PARAM_NAME=FLASK_LAB_SORT_PARAM_NAME,
            FLASK_LAB_PAGE_SIZE_PARAM_NAME=FLASK_LAB_PAGE_SIZE_PARAM_NAME,
            FLASK_LAB_OFFSET_PARAM_NAME=FLASK_LAB_OFFSET_PARAM_NAME,
            FLASK_LAB_LIMIT_PARAM_NAME=FLASK_LAB_LIMIT_PARAM_NAME,
            FLASK_LAB_FIELDS_PARAM_NAME=FLASK_LAB_FIELDS_PARAM_NAME,
        )
        for k, v in default_config.items():
            app.config.setdefault(k, v)

        endpoints_map = {}
        if isinstance(endpoints, list):
            for e in endpoints:
                e = ensure_endpoint(e)
                endpoints_map[slugify(e.name())] = e
        else:
            for k, v in endpoints.items():
                endpoints_map[k] = ensure_endpoint(v)

        for slug, endpoint in endpoints_map.items():
            e = endpoint()
            views = e.as_views()
            app.add_url_rule(
                f"{url_prefix}/{slug}",
                defaults=dict(pk=None),
                view_func=views,
                methods=["GET"],
            )
            app.add_url_rule(f"{url_prefix}/{slug}", view_func=views, methods=["POST"])
            app.add_url_rule(
                f"{url_prefix}/{slug}/<int:pk>",
                view_func=views,
                methods=["GET", "PUT", "DELETE"],
            )


"""
Command line app to generate restful service
"""


def add_restful_options(parser):
    parser.add_option(
        "-m",
        "--model-file",
        dest="model_file",
        default="flask_lab_models.py",
        help="Model filename to generate",
    )
    parser.add_option(
        "-a",
        "--app-file",
        dest="app_file",
        default="flask_lab_app.py",
        help="Flask App filename to generate",
    )
    parser.add_option(
        "-l",
        "--listen-address",
        dest="listen_address",
        default="0.0.0.0:5000",
        help="Port for flask app to listen on. Format: 0.0.0.0:5000",
    )
    parser.add_option(
        "-C",
        "--create-demo",
        dest="create_demo",
        action="store_true",
        help="Create a demo database with Article and User Model to demo Flask-Lab",
    )
    parser.add_option("-d", "--database", dest="database", help="Database to use")


def generate_app(app_file, model_file, listen_address):
    host, port = listen_address.split(":")
    model_file = model_file.split(".")[0]
    app_content = f"""from flask import Flask
from {model_file} import *
from flask_lab import FlaskLab


def create_app(conf=None):
    app = Flask(__name__)
    return app


def _find_models():
    from inspect import isclass
    from peewee import Model
    models = []
    for _, obj in globals().items():
        if isclass(obj) and issubclass(obj, Model) and obj != Model:
            models.append(obj)
    return models


if __name__ == '__main__':
    app = create_app()
    lab = FlaskLab()
    models = _find_models()
    lab.init_app(app, models)
    app.run(host="{host}", port={port}, debug=True)
"""
    with open(app_file, "w") as wf:
        wf.write(app_content)


def create_demo():
    import sqlite3
    from datetime import datetime

    conn = sqlite3.connect("flask_lab_demo.db")
    c = conn.cursor()
    c.execute(
        """
create table if not exists user (
    id integer not null primary key,
    name text not null
)"""
    )
    for i in range(1, 101):
        c.execute("insert into user (id, name) values (%d, 'user_%s')" % (i, i))
    c.execute(
        """
create table if not exists article (
    id integer not null primary key,
    title text not null,
    publish_time datetime not null,
    user_id interger not null,
    foreign key(user_id) references user(id)
)"""
    )
    for i in range(1, 11):
        c.execute(
            "insert into article (id, title, publish_time, user_id) values(?, ?, ?, ?)",
            (i, "Article Example %s" % i, datetime.now(), i),
        )
    conn.commit()
    conn.close()


def main():
    # XXX copy and pasted from peewee's pwiz module to parse args
    # see: https://github.com/coleifer/peewee/blob/master/pwiz.py#L197

    parser = get_option_parser()
    parser.usage = "%prog [options], %prog -h for detailed help"
    add_restful_options(parser)
    options, args = parser.parse_args()

    if options.create_demo:
        create_demo()
        return

    if not options.database:
        parser.print_usage()
        print("no database given")
        return

    from subprocess import check_output, CalledProcessError

    # call python -m pwiz to generate table. This is not pretty, I know.
    cmd = f"""python3 -m pwiz \
        {"--host "  + options.host if options.host else "" } \
        {"--port " + options.port if options.port else ""} \
        {"--user " + options.user if options.user else ""} \
        {"--password " + options.password if options.password else ""}\
        {"--engine " + options.engine if options.engine else ""}\
        {"--schema " + options.schema if options.schema else ""}\
        {"--tables " + options.tables if options.tables else ""}\
        {"--views" if options.views else ""} \
        {"--info" if options.info else ""} \
        {"--preserve-order" if options.preserve_order else ""} \
        {"--ignore-unknown" if options.ignore_unknown else ""} \
        {"--legacy_naming" if options.legacy_naming else ""} \
        {options.database} > {options.model_file}"""

    try:
        check_output(cmd, shell=True)
    except CalledProcessError:
        print("Generate model failed.")
        return
    generate_app(options.app_file, options.model_file, options.listen_address)
    print(
        f"Flask app and model files have been generated as {options.app_file} and {options.model_file}"
    )
    print(f"Starting server with command `python3 {options.app_file}`")
    os.system(f"python3 {options.app_file}")


if __name__ == "__main__":
    main()
