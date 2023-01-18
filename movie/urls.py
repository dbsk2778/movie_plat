from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    # 메인홈 URL
    path('movie/', views.movie, name='movie'),
<<<<<<< HEAD
=======

    # tv Show URL
    path('tvshow/',views.tvshow, name='tvshow'),

    # 장르선택 페이지 URL
    path('choice/', views.genre, name='choice'),

    # 
    path('usergenre/', views.usergenre, name='usergenre'),

    # 추천페이지 URL
    path('recommend/',views.movie_recommendation, name='recommend')
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f

    # tv Show URL
    path('tvshow/',views.tvshow, name='tvshow'),

    # 장르선택 페이지 URL
    path('choice/', views.genre, name='choice'),

    # 
    path('usergenre/', views.usergenre, name='usergenre'),

    # 추천페이지 URL
    path('recommend/',views.db_recommend, name='recommend'),

    # 콘텐츠 기반 추천
    path('content_recommend/',views.content_recommend, name='content_recommend'),
    
    # TMDB 추천
    path('tmdb_recommend/',views.tmdb_recommend, name='tmdb_recommend'),

    # meta_data 추천
    path('meta_recommend/',views.meta_recommend, name='meta_recommend'),
]
