from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from webhook.serializers import WebhookSerializer
from .models import Webhook


class GenericWebhookHandler(APIView):
    def handler(self, request, *args, **kwargs):
        webhook = Webhook.objects.create(
            scheme=request.remote_scheme,
            path=request.path,
            method=request.method,
            query_params=request.META.get('QUERY_STRING', ''),
            remote_address=request.remote_ip,
            remote_host=request.remote_host,
            headers=dict(request.headers),
            encoding=request.encoding,
            post_data=dict(request.POST.lists()),
        )
        return Response(data={'detail': webhook.rehook_id}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return self.handler(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.handler(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.handler(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.handler(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.handler(request, *args, **kwargs)


class WebhookViewSet(viewsets.ModelViewSet):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer
    lookup_field = 'rehook_id'
