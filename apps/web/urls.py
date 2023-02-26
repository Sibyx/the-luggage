from django.urls import path

from apps.web.views import changelog

urlpatterns = [

    path("changelog", changelog.Changelog.as_view(), name='changelog'),
]
