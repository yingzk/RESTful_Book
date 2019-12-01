# -*- coding: utf-8 -*-

__author__ = 'YingJoy'


class Redprint:

    def __init__(self, name):
        self.name = name
        self.mount = []

    def route(self, rule, **options):
        """register route"""
        def decorator(f):
            self.mount.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        """red print register"""
        if not url_prefix:
            url_prefix = '/' + self.name

        for f, rule, options in self.mount:
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
