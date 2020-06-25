from django.urls import include
from api import urls
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]


