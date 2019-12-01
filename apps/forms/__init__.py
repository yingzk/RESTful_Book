# -*- coding: utf-8 -*-

from wtforms import Form

from libs.error.error import ParameterError

__author__ = 'YingJoy'


class BaseForm(Form):
    def __init__(self, request):
        data = request.get_json(silent=True)
        args = request.args.to_dict()

        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterError(msg=self.errors)
        return self
