from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.movies_list, name="movies"),
    path("movies/<slug:slug>/", views.movie_detail, name="movie_detail"),
]
