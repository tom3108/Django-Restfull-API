from django.conf.urls import url, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet, basename="Movie")
router.register(r'rate', views.RateViewSet, basename="Rate")
router.register(r'actors', views.ActorViewSet, basename="Actor")


urlpatterns = [
    url('', include(router.urls))
]


