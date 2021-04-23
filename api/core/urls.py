from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import QuestionViewSet, OptionViewSet, MemberViewSet

router = routers.DefaultRouter()

router.register('questions', QuestionViewSet)
router.register('options', OptionViewSet)
router.register('members', MemberViewSet)


urlpatterns = [
    path('', include(router.urls))
]