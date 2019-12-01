# -*- coding: utf-8 -*-

from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = 'YingJoy'


class APIException(HTTPException):
    code = 500
    error_code = 9999
    msg = 'Sorry, we make a mistake'

    def __init__(self, code=None, error_code=None, msg=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(self.msg, None)

    def get_body(self, environ=None):
        body = dict(
            error_code=self.error_code,
            msg=self.msg,
            request=request.method + ' ' + APIException.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        return request.full_path.split('?')[0]
