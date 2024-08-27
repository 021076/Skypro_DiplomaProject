from django.urls import path

from testing.apps import TestingConfig
from testing.views import TestsListAPIView, TestsRetrieveAPIView, QuestionsAPIView

app_name = TestingConfig.name

urlpatterns = [
    path('tests/', TestsListAPIView.as_view(), name='tests-list'),
    path('tests/<int:pk>/', TestsRetrieveAPIView.as_view(), name='test'),
    path('tests/answer/', QuestionsAPIView.as_view(), name='test-answer'),
]
