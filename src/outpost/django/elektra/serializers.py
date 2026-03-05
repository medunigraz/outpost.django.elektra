import logging

from rest_flex_fields import FlexFieldsModelSerializer

from . import models

logger = logging.getLogger(__name__)


class ProjectReportSerializer(FlexFieldsModelSerializer):
    """
    ## Expansions

    To activate relation expansion add the desired fields as a comma separated
    list to the `expand` query parameter like this:

        ?expand=<field>,<field>,<field>,...

    The following relational fields can be expanded:

     * `sponsor`

    """
    class Meta:
        model = models.ProjectReport
        fields = "__all__"

    @property
    def expandable_fields(self):
        return {
            "sponsor": (
                "outpost.django.research.serializers.FunderSerializer",
                {"source": "sponsor"},
            )
        }


class ProjectReportTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.ProjectReportTask
        fields = "__all__"


class ProjectCalculationTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.ProjectCalculationTask
        fields = "__all__"


class ContractReviewTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.ContractReviewTask
        fields = "__all__"


class SponsorClearanceTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.SponsorClearanceTask
        fields = "__all__"


class AdministrationConfirmationTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.AdministrationConfirmationTask
        fields = "__all__"


class RectorateCommitmentTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.RectorateCommitmentTask
        fields = "__all__"


class MedicalBoardClearanceTaskSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.MedicalBoardClearanceTask
        fields = "__all__"
