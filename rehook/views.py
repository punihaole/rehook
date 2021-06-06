import logging

from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response


logger = logging.getLogger('rehook')


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        logger.info(f'{self.request.remote_ip} visited home page.')
        context = super().get_context_data(**kwargs)
        return context


class APIHealthView(generics.RetrieveAPIView):
    def get(self, request):
        return Response({}, status=200)
