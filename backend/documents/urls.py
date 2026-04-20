from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet) # This creates /api/documents/documents/
router.register(r'categories', CategoryViewSet) # This creates /api/documents/categories/

urlpatterns = [
    path('', include(router.urls)),
]