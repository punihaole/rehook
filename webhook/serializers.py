from rest_framework import routers, serializers, viewsets

from webhook.models import Webhook


class WebhookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='rehook_id')

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
            'date',
        ]
