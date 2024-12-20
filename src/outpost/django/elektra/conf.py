from appconf import AppConf
from django.conf import settings


class ElektraAppConf(AppConf):
    SCHEMA = "doxis"

    class Meta:
        prefix = "ELEKTRA"
