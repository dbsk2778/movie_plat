from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse
from .models import Genre, Movie, Usergenre, Like, genre_recommand4, StayTime
from .content_filter import find_sim_movie
from .meta_filter import meta_recommendations

import pandas as pd 
import warnings; warnings.filterwarnings('ignore')
from ast import literal_eval 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from django.core.paginator import Paginator

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


# 좋아요 함수
def likethis(request):
    # print(request.GET['title'])
    # print(request.GET['poster'])
    like_movie = Like.objects.filter(username=request.user.id)
    
    Like.objects.create(username =request.user.id, title = request.GET['title'], poster_path = request.GET['poster'] )

# naver login
def naverlogin(request):

    print(request.GET['email'])
    # request로 token을 가져오기 or url을 가져와서 access token 추출

    # token = "YOUR_ACCESS_TOKEN"
    # header = "Bearer " + token # Bearer 다음에 공백 추가
    # url = "https://openapi.naver.com/v1/nid/me"
    # request = urllib.request.Request(url)
    # request.add_header("Authorization", header)
    # response = urllib.request.urlopen(request)
    # rescode = response.getcode()
    # if(rescode==200):
    #     response_body = response.read()
    #     print(response_body.decode('utf-8'))
    # else:
    #     print("Error Code:" + rescode)

# detail 머문 시간 함수
def staytime(request):

    title = request.GET.get('title', False)

    StayTime.objects.create(title = request.GET.get('title', False), second = request.GET.get('second', False))
    
    context = {
            'title': title
        }
    
    return HttpResponse(context, "application/json")

# 하나의 영화에 머문 시간
@csrf_exempt
def staytimeread(request):

    if request.method == "GET":
        
        title = request.GET.get('title', False)

        # print(title)
        staytimeread = StayTime.objects.filter(title = title)    

        staytimeread = list(staytimeread.values())
        context = {
            'staytimeread': staytimeread
        }

    return JsonResponse(context)

def allmovies(request):

    # 넷플릭스
    netflix = pd.read_csv('netflix_movie.csv')
    
    netflix_items = []
    netflix_count = netflix['count_x'][:21].to_list()
    netflix_title = netflix['title'][:21].to_list()
    netflix_poster_path = netflix['poster'][:21].to_list()
    netflix_release_date = netflix['release_date'][:21].to_list()
    netflix_overview = netflix['over_view'][:21].to_list()
    
    # 디즈니 플러스
    disney = pd.read_csv('disney_movie.csv')
    
    disney_items = []
    disney_count = disney['count'][:21].to_list()
    disney_title = disney['title'][:21].to_list()
    disney_poster_path = disney['poster'][:21].to_list()
    disney_release_date = disney['release_date'][:21].to_list()
    disney_overview = disney['over_view'][:21].to_list()

    # 아마존 프라임
    amazon = pd.read_csv('amazon_movie.csv')
    
    amazon_items = []
    amazon_count = amazon['Unnamed: 0'][:21].to_list()
    amazon_title = amazon['title'][:21].to_list()
    amazon_poster_path = amazon['poster'][:21].to_list()
    amazon_release_date = amazon['release_date'][:21].to_list()
    amazon_overview = amazon['over_view'][:21].to_list()

    # Apple TV

    apple = pd.read_csv('apple_movie.csv')

    apple_items = []
    apple_count = apple['count'][:21].to_list()
    apple_title = apple['title'][:21].to_list()
    apple_poster_path = apple['poster'][:21].to_list()
    apple_release_date = apple['release_date'][:21].to_list()
    apple_overview = apple['over_view'][:21].to_list()

    for i in range(0, 21, 1):
        # 넷플릭스
        netflix_movie_dict = {
            "netflix_count" : netflix_count[i],
            "netflix_title" : netflix_title[i],
            "netflix_poster_path" : netflix_poster_path[i],
            "netflix_release_date" : netflix_release_date[i],
            "netflix_overview" : netflix_overview[i]
            }
        
        netflix_items.append(netflix_movie_dict)

        # 디즈니 플러스
        disney_movie_dict = {
            "disney_count" : disney_count[i],
            "disney_title" : disney_title[i],
            "disney_poster_path" : disney_poster_path[i],
            "disney_release_date" : disney_release_date[i],
            "disney_overview" : disney_overview[i]
            }
        
        disney_items.append(disney_movie_dict)

        # 아마존 프라임
        amazon_movie_dict = {
            "amazon_count" : amazon_count[i],
            "amazon_title" : amazon_title[i],
            "amazon_poster_path" : amazon_poster_path[i],
            "amazon_release_date" : amazon_release_date[i],
            "amazon_overview" : amazon_overview[i]
            }
        
        amazon_items.append(amazon_movie_dict)

        # Apple TV
        apple_movie_dict = {
            "apple_count": apple_count[i],
            "apple_title" : apple_title[i],
            "apple_poster_path" : apple_poster_path[i],
            "apple_release_date" : apple_release_date[i],
            "apple_overview" : apple_overview[i]
            }
        
        apple_items.append(apple_movie_dict)


    context = {
        "netfilx_items" : netflix_items,
        "disney_items": disney_items,
        "amazon_items" : amazon_items,
        "apple_items" : apple_items
                }
    return render(request, 'distributor/all_movies.html', context=context) 


# 넷플릭스 영화 보여주기
def netflix(request):  
    
    netflix = pd.read_csv('netflix_movie.csv')
    
    netflix_items = []
    title = netflix['title'].to_list()
    poster_path = netflix['poster'].to_list()
    release_date = netflix['release_date'].to_list()
    overview = netflix['over_view'].to_list()
    
    for i in range(0, 219, 1):
        movie_dict = {
            "title" : title[i],
            "poster_path" : poster_path[i],
            "release_date" : release_date[i],
            "overview" : overview[i]
            }
        
        netflix_items.append(movie_dict)

    paginator = Paginator(netflix_items, 24)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "netflix_items" : netflix_items,
        "posts":posts
                }
    return render(request, 'distributor/netflix.html', context=context) 

# 디즈니 플러스 영화 보여주기
def disneyplus(request):  
    disney = pd.read_csv('disney_movie.csv')
    
    disney_items = []
    title = disney['title'].to_list()
    poster_path = disney['poster'].to_list()
    release_date = disney['release_date'].to_list()
    overview = disney['over_view'].to_list()

    for i in range(0, 147, 1):
        movie_dict = {
            "title" : title[i],
            "poster_path" : poster_path[i],
            "release_date" : release_date[i],
            "overview" : overview[i]
            }
        
        disney_items.append(movie_dict)

    paginator = Paginator(disney_items, 24)

    page = request.GET.get('page')
    
    posts = paginator.get_page(page)


    context = {
        "disney_items" : disney_items,
        "posts":posts
                }
    return render(request, 'distributor/disneyplus.html' , context=context) 

# AmazonPrime 영화 보여주기
def amazonprime(request): 

    amazon = pd.read_csv('amazon_movie.csv')
    
    amazon_items = []
    title = amazon['title'].to_list()
    poster_path = amazon['poster'].to_list()
    release_date = amazon['release_date'].to_list()
    overview = amazon['over_view'].to_list()

    for i in range(0, 222, 1):
        movie_dict = {
            "title" : title[i],
            "poster_path" : poster_path[i],
            "release_date" : release_date[i],
            "overview" : overview[i]
            }
        
        amazon_items.append(movie_dict)
    
    paginator = Paginator(amazon_items, 24)

    page = request.GET.get('page')
    
    posts = paginator.get_page(page)

    context = {
        "amazon_items" : amazon_items,
        "posts": posts
                }
    return render(request, 'distributor/amazonprime.html', context=context) 

# Apple TV 영화 보여주기
@require_GET
def appletv(request):  
    
    apple = pd.read_csv('apple_movie.csv')

    apple_items = []
    title = apple['title'].to_list()
    poster = apple['poster'].to_list()
    release_date = apple['release_date'].to_list()
    overview = apple['over_view'].to_list()

    for i in range(0, 111, 1):
        movie_dict = {
            "title" : title[i],
            "poster" : poster[i],
            "release_date" : release_date[i],
            "overview" : overview[i]
            }
        
        apple_items.append(movie_dict)

    # 한페이지에 담길 객체 수 정의
    paginator = Paginator(apple_items, 24)

    page = request.GET.get('page')
    
    posts = paginator.get_page(page)

    context = {
        "apple_items" : apple_items,
        "posts" : posts
                }
    return render(request, 'distributor/appletv.html', context=context) 