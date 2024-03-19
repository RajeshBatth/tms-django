from django.contrib import admin

# Register your models here.
from .models import TestCaseModule, TestCase, TestRun, Report, TestCaseStatus

admin.site.register(TestCaseModule)
admin.site.register(TestCase)