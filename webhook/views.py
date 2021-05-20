from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from webhook.serializers import WebhookSerializer
from .models import Webhook


class GenericWebhookHandler(APIView):
    permission_classes = []
    authentication_classes = []

    def dispatch(self, request, *args, **kwargs):
        request._body = request.body
        return super().dispatch(request, *args, **kwargs)

    def handler(self, request, *args, **kwargs):
        data = dict(request.POST.lists())
        if not data:
            data = request.data
        body = request._body
        if isinstance(body, bytes):
            try:
                body = body.decode('utf-8')
            except UnicodeDecodeError:
                body = ''
        webhook = Webhook.objects.create(
            scheme=request.remote_scheme,
            path=request.path,
            method=request.method,
            query_params=request.META.get('QUERY_STRING', ''),
            remote_address=request.remote_ip,
            remote_host=request.remote_host,
            headers=dict(request.headers),
            encoding=request.encoding,
            data=data,
            body=body,
            body_raw=request._body,
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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class WebhookViewSet(viewsets.ModelViewSet):
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer
    lookup_field = 'rehook_id'
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['path', 'remote_address', 'date', ]
