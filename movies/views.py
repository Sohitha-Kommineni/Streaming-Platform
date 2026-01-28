from django.http import Http404
from django.shortcuts import render

from .data import MOVIES


def home(request):
    featured = MOVIES[0]
    trending = sorted(MOVIES, key=lambda movie: movie["rating"], reverse=True)[:6]
    category_names = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror"]
    categories = []
    for name in category_names:
        movies_in_category = [movie for movie in MOVIES if name in movie["genres"]][:4]
        if movies_in_category:
            categories.append({"name": name, "movies": movies_in_category})

    context = {
        "featured": featured,
        "trending": trending,
        "categories": categories,
    }
    return render(request, "home.html", context)


def movies_list(request):
    context = {"movies": MOVIES}
    return render(request, "movies.html", context)


def movie_detail(request, slug):
    movie = next((movie for movie in MOVIES if movie["slug"] == slug), None)
    if movie is None:
        raise Http404("Movie not found")
    related = [
        candidate
        for candidate in MOVIES
        if candidate["slug"] != movie["slug"]
        and any(genre in candidate["genres"] for genre in movie["genres"])
    ][:4]
    context = {"movie": movie, "related": related}
    return render(request, "movie_detail.html", context)
