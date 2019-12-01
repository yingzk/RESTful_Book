# -*- coding: utf-8 -*-
from flask import jsonify

from apps.models.user import UserModel
from libs.redprints import Redprint

__author__ = 'YingJoy'

api = Redprint('user')


@api.route('', methods=['GET'])
def get_user():
    u = UserModel.query.first_or_404().hide('password', 'amount')
    return jsonify(u)
