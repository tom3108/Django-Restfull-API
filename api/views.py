from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer
from .models import Movie
from .serializers import MovieSerializer, MovieMiniSerializer
from django.http.response import HttpResponseNotAllowed


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
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #if request.user.is_staff:
        movie = Movie.objects.create(title=request.data['title'],
                                         content=request.data['content'],
                                         after_prem=request.data['after_prem'])
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
        #else:
        #return HttpResponseNotAllowed('Not allowed')
    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.title = request.data['title']
        movie.content = request.data['content']
        movie.after_prem = request.data['after_prem']
        movie.save()
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()
        return Response('Deleted movie')



