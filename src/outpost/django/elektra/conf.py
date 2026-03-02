from appconf import AppConf
from django.conf import settings


class ElektraAppConf(AppConf):
    SCHEMA = "doxis"
    FDW_HOSTNAME = ""
    FDW_PORT = None
    FDW_DATABASE = ""
    FDW_USERNAME = ""
    FDW_PASSWORD = ""

    class Meta:
        prefix = "ELEKTRA"
