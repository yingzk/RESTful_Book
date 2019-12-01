# -*- coding: utf-8 -*-

__author__ = 'YingJoy'

from apps.models import db
from apps import create_app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.models.list import ModelList

app = create_app()

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
