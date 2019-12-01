# -*- coding: utf-8 -*-

from libs.error import APIException

__author__ = 'YingJoy'


class Success(APIException):
    code = 200
    error_code = 0
    msg = 'ok'
