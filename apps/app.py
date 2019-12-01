# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from libs.error.error import EncoderError

__author__ = 'YingJoy'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            print(o)
            return dict(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, Decimal):
            return float(o)
        raise EncoderError()


class Flask(_Flask):
    json_encoder = JSONEncoder
