# -*- coding: utf-8 -*-

__author__ = 'YingJoy'

from flask import Blueprint
from apps.api.v1 import user, book, client


def create_blueprint():
    v1_bp = Blueprint('v1', __name__)

    user.api.register(v1_bp)
    book.api.register(v1_bp)
    client.api.register(v1_bp)

    return v1_bp
