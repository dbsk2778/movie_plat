from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    # 메인홈 URL
    path('movie/', views.movie, name='movie'),

    # tv Show URL
    path('tvshow/',views.tvshow, name='tvshow'),

    # 장르선택 페이지 URL
    path('choice/', views.genre, name='choice'),

    # 
    path('usergenre/', views.usergenre, name='usergenre'),

    # 추천페이지 URL
    path('recommend/',views.movie_recommendation, name='recommend')

]
