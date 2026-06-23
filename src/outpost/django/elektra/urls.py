from django.conf.urls import url

from . import views

app_name = "elektra"

urlpatterns = [
    url(r"^xml$", views.ProjectImportView.as_view(), name="xml"),
]
