# app/urls.py
from django.urls import path
from .views import TestCaseListView

urlpatterns = [
    path('test-cases/', TestCaseListView.as_view(), name='test-case-list'),
]
