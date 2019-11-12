from django.db import models
from django.utils.baseconv import base36


class Base36IntegerField(models.BigIntegerField):
    def __init__(self, prefix='', *args, **kwargs):
        self.prefix = prefix
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwarg if it's not the default
        if self.prefix != '':
            kwargs['prefix'] = self.prefix
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context=None):
        if value is None:
            return value
        return self.encode(value)

    def get_prep_value(self, value):
        if value is None or isinstance(value, int):
            return value
        return self.decode(value)

    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, str):
            return value
        return self.encode(value)

    def decode(self, value):
        value = value.replace(self.prefix, '')
        pos_id = base36.decode(value)
        raw_id = pos_id - 2**63
        return raw_id

    def encode(self, raw_value):
        pos_id = raw_value + 2**63
        encoded_id = base36.encode(pos_id)
        return f'{self.prefix}{encoded_id}'
