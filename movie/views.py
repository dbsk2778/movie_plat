from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse
<<<<<<< HEAD
from .models import Genre,Movie, Usergenre, Like, genre_recommand4
from .content_filter import find_sim_movie
from .meta_filter import meta_recommendations
=======
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
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f

import pandas as pd 
import warnings; warnings.filterwarnings('ignore')
from ast import literal_eval 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

from django.shortcuts import render


def tmdb_recommend(request):

    if request.method == 'GET':

        title = request.GET.get('recom')

        movies= pd.read_csv('end_movies.csv')
        movies_df = movies[['id','title']]
    
        title_movie = movies_df[movies_df['title'] == title]

        tmdb_movie_id = title_movie['id'].to_list()

        context = {
            "tmdb_movie_id": tmdb_movie_id
        }
    return render(request, 'recommend/tmdb_recommend.html', context=context)
    # return render(request, 'recommend/db_recommend.html', context=context)

# 머신러닝 모듈은 검색 시 학습하기 때문에 시간이 소요될 수 있음
def content_recommend(request):

    # request.GET.get('recom')의 결과값이 있을 경우(콘텐츠 기반 필터링) if문 + 영화 배우 기반 추천 서비스 else문 (recom2) 해서 만드는 게 가능? 
    if request.method == 'GET':
        title = request.GET.get('recom')

        # ML 모델을 통해 추천 결과 획득
        similar_movies = find_sim_movie(title) 
        
        movie_list = []
        
        movie_id = similar_movies['id'][:21].to_list()
        title = similar_movies['title'][:21].to_list()
        poster_path = similar_movies['poster_path'][:21].to_list()
        
        for i in range(0, 21, 1):
            movie_dict = {
                "movie_id" : movie_id[i],
                "title" : title[i],
                "poster_path" : poster_path[i]}
            
            movie_list.append(movie_dict)

        context = {
            "items" : movie_list
                    }
        return render(request, 'recommend/content_recommend.html', context=context)
        # return render(request, 'recommend/db_recommend.html', context=context)

def meta_recommend(request):

    # request.GET.get('recom')의 결과값이 있을 경우(콘텐츠 기반 필터링) if문 + 영화 배우 기반 추천 서비스 else문 (recom2) 해서 만드는 게 가능? 
    if request.method == 'GET':
        title = request.GET.get('recom')

        # ML 모델을 통해 추천 결과 획득
        similar_movies = meta_recommendations(title) 
        
        movie_id = similar_movies['id'][:21].to_list()
        
        movie_dict = {
            "movie_id" : movie_id,
            }

        context = {
            "items" : movie_dict
                    }

        return render(request, 'recommend/meta_recommend.html', context=context)

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
<<<<<<< HEAD


def db_recommend(request):
    # 현재 로그인한 사용자가 좋아한다고 체크했던 장르 데이터들을 가져옴
    user_favorite_genres = Usergenre.objects.filter(username_id=request.user.id)

    # 추천 영화 데이터들을 저장할 변수 선언
    result = Movie.objects.none()

    # 좋아한다고 체크했던 장르들이 여러 개일 수 있으니 반복문으로 처리
    for favorite_genre in user_favorite_genres:
        # 좋아한다고 체크했던 장르의 ID를 이용해서 해당 장르의 추천 영화들을 가져옴
        recommend_movie_list = genre_recommand4.objects.filter(genre_id=favorite_genre.genre_id)

        for recommend_movie in recommend_movie_list:
            movie = Movie.objects.filter(pk=recommend_movie.movie_id)
            result |= movie

    print("추천영화들:", result)
    context = {
        'user_movieId': result,
    }

    return render(request, 'recommend/db_recommend.html', context)
=======
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
