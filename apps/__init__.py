# -*- coding: utf-8 -*-

from .app import Flask

from apps.models import db
from libs.error import APIException
from libs.error.error import ServerError
from werkzeug.exceptions import HTTPException

from apps.api.v1 import create_blueprint as v1_bp

__author__ = 'YingJoy'


def create_app():
    app = Flask(__name__)

    # import config
    app.config.from_object('config.setting')
    app.config.from_object('config.security')
    
    # register blueprint
    register_blueprint(app)

    # register hooks
    register_hooks(app)

    # register plugins
    db.init_app(app)

    return app


def register_blueprint(app):
    app.register_blueprint(v1_bp(), url_prefix='/v1')


def register_hooks(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e
        if isinstance(e, HTTPException):
            return APIException(e.code, 1007, e.description)
        else:
            if app.config['DEBUG']:
                return e
            return ServerError()
