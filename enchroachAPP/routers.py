from django.urls import path,include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from .views import encroachments
router.register(r'encroachments',encroachments,basename='encroachments')