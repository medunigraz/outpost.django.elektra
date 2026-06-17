from django.core.cache import cache
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions

from .conf import settings
from .tasks import ElektraTasks


class ProjectImportView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        response = HttpResponse()
        response["Content-Type"] = "application/xml"
        xml = cache.get(settings.ELEKTRA_PROJECT_IMPORT_CACHE_KEY, None)
        if not xml:
            xml = ElektraTasks().generate()
        response.write(xml)
        return response
