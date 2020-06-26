from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Movie
from .serializers import MovieSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer


    def get_queryset(self):
        qs = Movie.objects.filter(after_prem=True)
        return qs


