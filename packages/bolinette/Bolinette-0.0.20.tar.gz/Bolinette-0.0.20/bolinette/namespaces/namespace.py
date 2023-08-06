import json
from functools import wraps

from flask import Blueprint, Response

from bolinette.namespaces import Defaults


class Namespace:
    namespaces = []

    def __init__(self, service, url):
        self.service = service
        self.model = service.name
        self.blueprint = Blueprint(self.model, __name__, url_prefix='/api' + url)

    @staticmethod
    def init_namespaces(app):
        for namespace in Namespace.namespaces:
            app.register_blueprint(namespace)

    def route(self, rule, **options):
        def wrapper(func):
            endpoint = options.pop("endpoint", func.__name__)
            self.blueprint.add_url_rule(rule, endpoint, func, **options)

            @wraps(func)
            def inner(*args, **kwargs):
                res, code = func(*args, **kwargs)
                return Response(json.dumps(res), code, mimetype='application/json')

            return inner

        return wrapper

    def register(self):
        Namespace.namespaces.append(self.blueprint)
    
    @property
    def defaults(self):
        return Defaults(self)
