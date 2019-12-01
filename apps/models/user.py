# -*- coding: utf-8 -*-
from sqlalchemy.dialects.mysql import TINYINT, DECIMAL
from werkzeug.security import generate_password_hash

from apps.models import db, BaseModel

__author__ = 'YingJoy'


class UserModel(BaseModel):
    __tablename__ = 'user'
    __table_args__ = {
        'comment': '用户表'
    }

    name = db.Column(db.String(20), nullable=False, comment='用户名')
    gender = db.Column(TINYINT(unsigned=True), default=0, nullable=False, comment='性别')
    amount = db.Column(DECIMAL(scale=2), default=0, comment='资产')
    _password = db.Column(db.String(128), name='password', nullable=False, comment='密码，SHA加密')
    type = db.Column(db.SmallInteger, default=1, nullable=False, comment='用户类型')
    status = db.Column(db.SmallInteger, default=1, nullable=False, comment='用户状态')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register(**kwargs):
        with db.auto_commit():
            print(kwargs)
            user = UserModel(
                name=kwargs['name'], gender=kwargs['gender'],
                amount=kwargs['amount'], type=kwargs['type'],
                status=kwargs['status']
            )
            user.password = kwargs['password']
            db.session.add(user)
