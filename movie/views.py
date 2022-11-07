from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http.response import JsonResponse
from .models import Movie, Genre


@require_GET
def movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie.html', context)


# @require_GET
# def detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     comments = movie.moviereview_set.all()
#     movie_comment_form = MovieReviewForm()
#     context = {
#         'movie': movie,
#         'movie_comment_form': movie_comment_form,
#         'comments': comments,
#     }
#     return render(request, 'movies/detail.html', context)


# @require_GET
# def recommend(request):
#     movies = Movie.objects.all()
#     context = {
#         'movies': movies,
#     }
#     return render(request, 'movies/recommend.html', context)


# @require_GET
# def recommendpopularity(request):
#     if request.user.is_authenticated:
#         movies = Movie.objects.order_by('-popularity')[:20]
#         context = {
#             'movies':movies,
#         }
#         return render(request, 'movies/recommendpopularity.html', context)
#     return render(request, 'accounts/login.html', context)


# @require_GET
# def recommendvoteaverage(request):
#     if request.user.is_authenticated:
#         movies = Movie.objects.order_by('-vote_average')[:20]
#         context = {
#             'movies':movies,
#         }
#         return render(request, 'movies/recommendvoteaverage.html', context)
#     return render(request, 'accounts/login.html', context)


@require_GET
def genre(request):
    # if request.user.is_authenticated:
    if request.GET.get('genreId'):
        genrebox = request.GET.get('genreId')
        movies = Movie.objects.filter(genre_ids=genrebox)
        movies_json = []

        for movie in movies:
            movies_json.append({
                'title': movie.title,
            })
        return JsonResponse({'text': movies_json})

    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'movies/recommendgenre.html', context)
    # return render(request, 'accounts/login.html', context)

