# -*- coding: utf-8 -*-
from libs.error import APIException

__author__ = 'YingJoy'


class Success(APIException):
    code = 200
    error_code = 0
    msg = 'ok'


class ServerError(APIException):
    code = 500
    error_code = 9999
    msg = 'Server Error'


class NotFound(APIException):
    code = 404
    error_code = 1001
    msg = 'The resource is not founded'


class ParameterError(APIException):
    code = 400
    error_code = 1002
    msg = 'invalid parameter'
