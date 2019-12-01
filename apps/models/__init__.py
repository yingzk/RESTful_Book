# -*- coding: utf-8 -*-

from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as SQLAlchemy_, BaseQuery
from sqlalchemy.dialects.mysql import BIGINT

from libs.error.error import NotFound

__author__ = 'YingJoy'


class SQLAlchemy(SQLAlchemy_):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'is_deleted' not in kwargs:
            kwargs['is_deleted'] = 0
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, description=None):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self, description=None):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True, comment='主键ID')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    is_deleted = db.Column(db.SmallInteger, nullable=False, default=0, comment='逻辑删除')

    def delete(self):
        self.is_deleted = 1

    def __getitem__(self, item):
        return getattr(self, item)
