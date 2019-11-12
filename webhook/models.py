import hashlib

from django.contrib.postgres.fields import HStoreField, JSONField
from django.db import models
from django.utils import timezone

from .fields import Base36IntegerField


class Webhook(models.Model):
    scheme = models.CharField(max_length=8, null=True, blank=True)
    path = models.CharField(max_length=255, null=False, blank=False)
    method = models.CharField(max_length=8, null=True, blank=True)
    query_params = models.CharField(max_length=255, null=False, blank=True)
    remote_address = models.CharField(max_length=45, null=False, blank=False)
    remote_host = models.CharField(max_length=255, null=True, blank=True)
    headers = HStoreField()
    encoding = models.CharField(max_length=255, null=True, blank=True)
    post_data = JSONField(null=True)
    date = models.DateTimeField(auto_now=True, db_index=True)
    rehook_id = Base36IntegerField(prefix='wh_', db_index=True, unique=True, null=False, blank=False)

    @property
    def user_agent(self):
        return self.headers['User-Agent']

    def generate_id(self):
        def int2bytes(x: int) -> bytes:
            return x.to_bytes((x.bit_length() + 7) // 8, 'big')

        h = hashlib.blake2b()
        h.update(self.remote_address.encode())
        h.update(self.path.encode())
        if self.date:
            date = self.date
        else:
            date = timezone.now()
        h.update(int2bytes(int(date.timestamp() * 1000000)))
        d = h.digest()[:8]
        bb = int.from_bytes(d, byteorder='big', signed=True)
        assert (bb.bit_length() <= 64)
        self.rehook_id = self._meta.get_field('rehook_id').to_python(bb)

    def save(self, *args, **kwargs):
        if not self.rehook_id:
            self.generate_id()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.rehook_id} {self.method} {self.path} from {self.remote_host}'
