from outpost.django.base.decorators import docstring_format
from outpost.django.base.mixins import CacheResponseMixin
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import (
    models,
    serializers,
)


@docstring_format(
    model=models.ProjectReport.__doc__,
    serializer=serializers.ProjectReportSerializer.__doc__,
)
class ProjectReportViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.ProjectReport.objects.all()
    serializer_class = serializers.ProjectReportSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.ProjectReportTask.__doc__,
    serializer=serializers.ProjectReportTaskSerializer.__doc__,
)
class ProjectReportTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.ProjectReportTask.objects.all()
    serializer_class = serializers.ProjectReportTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.ProjectCalculationTask.__doc__,
    serializer=serializers.ProjectCalculationTaskSerializer.__doc__,
)
class ProjectCalculationTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.ProjectCalculationTask.objects.all()
    serializer_class = serializers.ProjectCalculationTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.ContractReviewTask.__doc__,
    serializer=serializers.ContractReviewTaskSerializer.__doc__,
)
class ContractReviewTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.ContractReviewTask.objects.all()
    serializer_class = serializers.ContractReviewTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.SponsorClearanceTask.__doc__,
    serializer=serializers.SponsorClearanceTaskSerializer.__doc__,
)
class SponsorClearanceTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.SponsorClearanceTask.objects.all()
    serializer_class = serializers.SponsorClearanceTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.AdministrationConfirmationTask.__doc__,
    serializer=serializers.AdministrationConfirmationTaskSerializer.__doc__,
)
class AdministrationConfirmationTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.AdministrationConfirmationTask.objects.all()
    serializer_class = serializers.AdministrationConfirmationTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.RectorateCommitmentTask.__doc__,
    serializer=serializers.RectorateCommitmentTaskSerializer.__doc__,
)
class RectorateCommitmentTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.RectorateCommitmentTask.objects.all()
    serializer_class = serializers.RectorateCommitmentTaskSerializer
    permission_classes = (DjangoModelPermissions,)


@docstring_format(
    model=models.MedicalBoardClearanceTask.__doc__,
    serializer=serializers.MedicalBoardClearanceTaskSerializer.__doc__,
)
class MedicalBoardClearanceTaskViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    """
    List .

    {model}
    {serializer}
    """

    queryset = models.MedicalBoardClearanceTask.objects.all()
    serializer_class = serializers.MedicalBoardClearanceTaskSerializer
    permission_classes = (DjangoModelPermissions,)
