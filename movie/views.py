from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http.response import JsonResponse
from .models import Genre,Movie,genre_recommand4, Usergenre


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


def recommand(request):
    # 현재 로그인한 사용자가 좋아한다고 체크했던 장르 데이터들을 가져옴
    user_favorite_genres = Usergenre.objects.filter(username_id=request.user.id)

    # 추천 영화 데이터들을 저장할 변수 선언
    result = Movie.objects.none()

    # 좋아한다고 체크했던 장르들이 여러 개일 수 있으니 반복문으로 처리
    for favorite_genre in user_favorite_genres:
        # 좋아한다고 체크했던 장르의 ID를 이용해서 해당 장르의 추천 영화들을 가져옴
        recommand_movie_list = genre_recommand4.objects.filter(genre_id=favorite_genre.genre_id)

        for recommand_movie in recommand_movie_list:
            movie = Movie.objects.filter(pk=recommand_movie.movie_id)
            result |= movie

    print("추천영화들:", result)
    context = {
        'user_movieId': result,
    }

    return render(request, 'movie/recommand.html', context)
