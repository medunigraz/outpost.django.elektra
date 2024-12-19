import logging

from django.contrib.gis.db import models
from django.contrib.postgres.fields import (
    ArrayField,
    HStoreField,
)

logger = logging.getLogger(__name__)


class ProjectReport(models.Model):
    """
    Project report.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.PositiveIntegerField(primary_key=True)
    uuid = models.UUIDField()
    short = models.TextField()
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    type = models.TextField(null=True)
    planned_start = models.DateField(null=True)
    planned_end = models.DateField(null=True)
    research_type = models.TextField(null=True)
    organization = models.ForeignKey(
        "campusonline.Organization",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    subproject = models.BooleanField(null=True)
    internal_funds = models.BooleanField(null=True)
    investigator_initiated = models.BooleanField(null=True)
    leader = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    mentor = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    planned_total = models.PositiveIntegerField(null=True)
    title = HStoreField()
    clinical_phase = models.TextField(null=True)
    study_design = models.BooleanField(null=True)
    multi_national = models.BooleanField(null=True)
    sponsor = models.TextField(null=True)
    research_fields = ArrayField(models.TextField(null=True))
    cooperation_criteria = models.TextField(null=True)
    study_types = ArrayField(models.TextField(null=True))
    status = models.TextField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    effective_start = models.DateField(null=True)
    effective_end = models.DateField(null=True)
    internal_job_number = models.TextField(null=True)
    effective_total = models.PositiveIntegerField(null=True)
    abstract = HStoreField()

    class Meta:
        managed = False
        db_table = "elektra_project_report"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class ProjectReportTask(models.Model):
    """
    Project report task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_project_report_task"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class ProjectCalculationTask(models.Model):
    """
    Project calculation task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_project_calculation_task"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class ContractReviewTask(models.Model):
    """
    Contract review task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_contract_review_task"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class SponsorClearanceTask(models.Model):
    """
    Sponsor clearance task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_sponsor_clearance_task"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class AdministrationConfirmationTask(models.Model):
    """
    Administration confirmation task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_administration_confirmation"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class RectorateCommitmentTask(models.Model):
    """
    Rectorate commitment task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_rectorate_commitment"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)


class MedicalBoardClearanceTask(models.Model):
    """
    Medical board clearance task.

    ## Fields

    ### `id` (`integer`)
    Primary key.

    """

    id = models.CharField(primary_key=True, max_length=128)
    uuid = models.UUIDField()
    project_report = models.ForeignKey(
        "ProjectReport",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    administration = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    version = models.PositiveIntegerField()
    created = models.DateTimeField()
    workflow_accepted = models.DateTimeField(null=True)
    workflow_accepted_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_basket = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_finished = models.DateTimeField(null=True)
    workflow_finished_by = models.ForeignKey(
        "campusonline.Person",
        on_delete=models.DO_NOTHING,
        related_name="+",
        db_constraint=False,
        db_index=False,
        null=True,
        blank=True,
    )
    workflow_user_info = models.TextField(null=True)
    workflow_task_code = models.TextField(null=True)
    workflow_task_name = models.TextField(null=True)
    workflow_decision_code = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "elektra_medica_board_clearance"

    class Refresh:
        interval = 86400

    def __str__(self):
        return str(self.uuid)
