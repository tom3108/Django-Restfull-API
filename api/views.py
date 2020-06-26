from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer
from .models import Movie
from .serializers import MovieSerializer, MovieMiniSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    def get_queryset(self):
        qs = Movie.objects.filter(after_prem=True)
        return qs
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MovieMiniSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)


