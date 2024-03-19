from django.db import models
from django.contrib.auth.models import User


class TestCaseModule(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    class Priority(models.TextChoices):
        HIGH = "HIGH", "High"
        DEFAULT = "DEFAULT", "Default"
        LOW = "LOW", "Low"

    test_id = models.CharField(primary_key=True, max_length=255)
    module = models.ForeignKey(TestCaseModule, on_delete=models.CASCADE)
    created = models.DateField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.DEFAULT
    )
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_archived = models.BooleanField(default=False)
    issue_tracker_ids = models.JSONField(default=list)

    def __str__(self):
        return self.module.name + "-" + self.test_id + " :: " + self.name


class TestRun(models.Model):
    id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    branch_head = models.CharField(max_length=255)
    triggered_by_user = models.CharField(max_length=255)
    ci_job_id = models.CharField(max_length=255)
    browser_info = models.TextField()
    view_port_size = models.CharField(max_length=255)


class Report(models.Model):
    test_run_id = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    time_taken = models.DurationField()
    new_tests_added = models.IntegerField()
    tests_skipped = models.IntegerField()
    tests_completed = models.IntegerField()
    tests_failed = models.IntegerField()


class TestCaseStatus(models.Model):
    class Meta:
        verbose_name = "TestCaseStatus"
        verbose_name_plural = "TestCaseStatuses"

    test_run_id = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    test_id = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    time_taken = models.DurationField()
    errors = models.TextField()
    attachments = models.JSONField(default=list)
