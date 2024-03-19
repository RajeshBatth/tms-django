from rest_framework import serializers
from .models import TestCase, TestRun, Report, TestCaseStatus, TestCaseModule
from django.contrib.auth.models import User

class TestCaseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseModule
        fields = '__all__'

class TestCaseSerializer(serializers.ModelSerializer):
    module = TestCaseModuleSerializer()

    class Meta:
        model = TestCase
        fields = '__all__'

class TestRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRun
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class TestCaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseStatus
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
