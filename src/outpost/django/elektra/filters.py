from functools import reduce
from operator import or_

from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_filters import DateFilter
from django_filters.rest_framework import filterset

from . import models
from .conf import settings


class ProjectReportFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    Possible exact filters:

      - `created`

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    All fields with advanced lookups can also be used for exact value matches
    as described above.

    Possible advanced lookups:

      - `created`: `date`
    """

    class Meta:
        model = models.ProjectReport
        fields = {
            "created": ("exact", "gt", "lt", "gte", "lte", "date"),
        }