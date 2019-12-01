# -*- coding: utf-8 -*-
from flask import request

from apps.forms.client import RegisterForm
from apps.models.user import UserModel
from libs.error.error import Success
from libs.redprints import Redprint

__author__ = 'YingJoy'

api = Redprint('client')


@api.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request).validate_for_api()

    UserModel.register(**form.data)

    return Success()
