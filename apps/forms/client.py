# -*- coding: utf-8 -*-
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, length

from apps.enums.user import UserTypeEnum
from apps.forms import BaseForm

__author__ = 'YingJoy'


class RegisterForm(BaseForm):
    name = StringField(validators=[DataRequired(message='name is required'), length(min=1, max=18)])
    gender = IntegerField()
    amount = DecimalField()
    password = StringField(validators=[DataRequired()])
    type = IntegerField(validators=[DataRequired()])
    status=IntegerField()

    def validate_type(self, value):
        try:
            type = UserTypeEnum(value.data)
        except ValueError as e:
            raise e

        self.type.data = type.value
