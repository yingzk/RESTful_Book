# -*- coding: utf-8 -*-
from libs.redprints import Redprint

__author__ = 'YingJoy'

api = Redprint('user')


@api.route('')
def user():
    return 'user'
