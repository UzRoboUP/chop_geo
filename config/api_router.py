from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter


router = DefaultRouter() if settings.DEBUG else SimpleRouter()


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("trajectories/", include('chop_geo.trajectories.urls'), name='trajectories'),
    path("bluetooth/", include('chop_geo.bluetooth.urls'), name='bluetooth'),
    path("users/", include('chop_geo.users.urls'), name='users'),
]
