from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse
from .models import Genre,Movie, Usergenre, Like
from .content_filter import find_sim_movie

import pandas as pd 
import warnings; warnings.filterwarnings('ignore')
from ast import literal_eval 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

from django.shortcuts import render

# 머신러닝 모듈은 장고 runserver 실행될 때 자동으로 한번 실행되어, 시간이 소요될 수 있음
def movie_recommendation(request):

    if request.method == 'GET':
        title = request.GET.get('recom')

        # ML 모델을 통해 추천 결과 획득
        similar_movies = find_sim_movie(title) 
        
        movie_list = []
        
        movie_id = similar_movies['id'][:10].to_list()
        title = similar_movies['title'][:10].to_list()
        poster_path = similar_movies['poster_path'][:10].to_list()
        
        for i in range(0, 10, 1):
            movie_dict = {
                "movie_id" : movie_id[i],
                "title" : title[i],
                "poster_path" : poster_path[i]}
            
            movie_list.append(movie_dict)

        context = {
            "items" : movie_list
                    }
            
        return render(request, 'movie/recommend.html', context=context)


@require_GET
def movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie.html', context)
@require_GET

def tvshow(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/tvshow.html', context)

@require_GET
def genre(request):
    select_genre = Usergenre.objects.filter(username_id=request.user.id)
    
    # 장르 선택이 되어있으면 홈으로 이동
    if select_genre.exists():
        return render(request, 'movie/movie.html')
    
    # 장르 선택이 되어있지 않으면 choice로 이동
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
