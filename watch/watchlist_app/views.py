from django.shortcuts import render
from watchlist_app.models import Movie
# Create your views here.
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies':list(movies.values())}
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk= pk)
    print(movie.name)
    data = {'name':movie.name,
            'description': movie.desciption,
            'active': movie.active
            }
    return JsonResponse(data)