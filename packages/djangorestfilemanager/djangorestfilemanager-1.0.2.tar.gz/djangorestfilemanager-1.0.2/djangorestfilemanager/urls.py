from django.urls import include
from django.conf.urls import url
from rest_framework import routers

from djangorestfilemanager.views import FileModelViewSet

router = routers.DefaultRouter()
router.register(r'files', FileModelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
