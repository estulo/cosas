from django.urls import path
from django.urls.resolvers import URLPattern
from movies import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>/', views.MovieDetail.as_view()),
    path('movies/<int:pk>/reviews', views.ReviewList.as_view()),
    path('movies/<int:fk>/reviews/<int:pk>', views.ReviewDetail().as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)