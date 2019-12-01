# -*- coding: utf-8 -*-

__author__ = 'YingJoy'

from apps import create_app

app = create_app()


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=4444
    )
