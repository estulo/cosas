from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
]
