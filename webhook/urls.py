from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import WebhookViewSet

router = routers.DefaultRouter()
router.register(r'webhooks', WebhookViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]

