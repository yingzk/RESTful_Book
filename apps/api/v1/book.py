# -*- coding: utf-8 -*-

from libs.redprints import Redprint

__author__ = 'YingJoy'

api = Redprint('book')


@api.route('')
def book():
    return 'book'
