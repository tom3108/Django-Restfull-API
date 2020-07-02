from django.contrib import admin
from .models import Movie, ExtraInfo, Rate

admin.site.register(Movie)
admin.site.register(ExtraInfo)
admin.site.register(Rate)