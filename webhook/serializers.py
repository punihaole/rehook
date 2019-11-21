import base64

from django.db import models
from rest_framework import routers, serializers, viewsets

from webhook.models import Webhook


class WebhookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='rehook_id')
    body_base64 = serializers.SerializerMethodField()

    class Meta:
        model = Webhook
        fields = [
            'id',
            'scheme',
            'path',
            'method',
            'query_params',
            'remote_address',
            'remote_host',
            'headers',
            'encoding',
            'data',
            'body',
            'body_base64',
            'date',
        ]

    def get_body_base64(self, instance):
        try:
            return base64.b64encode(instance.body_raw).decode('utf-8')
        except TypeError:
            return None
