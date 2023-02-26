from django.conf import settings
from django.utils import timezone
from django.views import View

from apps.api.response import SingleResponse


class StatusManagement(View):
    def get(self, request):

        response = {
            'timestamp': timezone.now(),
            'instance': settings.INSTANCE_NAME,
            'build': settings.BUILD,
            'version': settings.VERSION
        }
        return SingleResponse(request, response)
