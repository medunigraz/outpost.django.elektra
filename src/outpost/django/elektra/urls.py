from django.urls import path

from . import views

app_name = "elektra"

urlpatterns = [
    path("xml/", views.ProjectImportView.as_view(), name="xml"),
]
