from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestCase
from .serializers import TestCaseSerializer

class TestCaseListView(APIView):
    def get(self, request):
        test_cases = TestCase.objects.all()
        serializer = TestCaseSerializer(test_cases, many=True)
        return Response(serializer.data)
