from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"projects", ProjectViewSet)

urlpatterns = [

    path("", include(router.urls)),
]