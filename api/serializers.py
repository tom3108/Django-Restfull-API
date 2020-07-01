from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['time', 'kind']

class MovieSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'content', 'after_prem',
                  'premiere','year','imdb_rating','name','extra_info']



