from django.core.cache import cache
from django.http import HttpResponse
from outpost.django.api.authentication import BearerTokenAuthentication
from outpost.django.api.permissions import ExtendedDjangoModelPermissions
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.views import APIView

from .conf import settings
from .models import ProjectImport
from .tasks import ElektraTasks


class ProjectImportView(APIView):

    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [ExtendedDjangoModelPermissions]
    queryset = ProjectImport.objects.all()
    renderer_classes = [XMLRenderer]

    def get(self, request):
        response = HttpResponse()
        response["Content-Type"] = "application/xml"
        xml = cache.get(settings.ELEKTRA_PROJECT_IMPORT_CACHE_KEY, None)
        if not xml:
            xml = ElektraTasks().generate()
        response.write(xml)
        return response
