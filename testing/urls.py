from django.urls import path
from rest_framework.routers import DefaultRouter

from testing.apps import TestingConfig
from testing.views import TestsListAPIView, TestsRetrieveAPIView, QuestionsAPIView

app_name = TestingConfig.name

router = DefaultRouter()

urlpatterns = [
    path('tests/', TestsListAPIView.as_view(), name='tests-list'),
    path('tests/<int:pk>/', TestsRetrieveAPIView.as_view(), name='test'),
    path('tests/answer/', QuestionsAPIView.as_view(), name='test-answer'),
] + router.urls
