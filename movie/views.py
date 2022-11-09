from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http.response import JsonResponse
from .models import Movie, Genre, Usergenre


@require_GET
def movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie.html', context)


@require_GET
def genre(request):
    select_genre = Usergenre.objects.filter(username_id=request.user.id)

    if select_genre.exists():
        return render(request, 'movie/movie.html')
    else:
        genres = Genre.objects.all() 
        context = {
        'genres': genres,
        }
        return render(request, 'movie/choice.html', context)


def usergenre(request):
    usergenre = request.POST.getlist('genre')
    
    for genre_id in usergenre:
        Usergenre.objects.create(genre_id=genre_id, username_id=request.user.id)

    return render(request, 'movie/movie.html')


