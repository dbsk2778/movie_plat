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
    path('recommend/',views.db_recommend, name='recommend'),

    # 콘텐츠 기반 추천
    path('content_recommend/',views.content_recommend, name='content_recommend'),
    
    # TMDB 추천
    path('tmdb_recommend/',views.tmdb_recommend, name='tmdb_recommend'),

    # meta_data 추천
    path('meta_recommend/',views.meta_recommend, name='meta_recommend'),

    # 프로필 좋아요
    path('likethis/', views.likethis, name = 'likethis'),

    # 네이버 자동 로그인 API DB 저장
    path('naverLogin/', views.naverlogin, name='naverlogin'),

    # detail 머문 시간
    path('staytime/', views.staytime, name = 'staytime'),

    # detail 머문 시간 출력
    path('staytimeread/', views.staytimeread, name = 'staytimeread'),

    # 제작사: 모든 제작사 영화 출력 
    path('allmovies/', views.allmovies, name = 'allmovies'),

    # 제작사: 넷플릭스 영화 출력 
    path('netflix/', views.netflix, name = 'netflix'), 

    # 제작사: 디즈니 플러스 영화 출력 
    path('disneyplus/', views.disneyplus, name = 'disneyplus'),

    # 제작사: 아마존 프라임 영화 출력 
    path('amazonprime/', views.amazonprime, name = 'amazonprime'),

    # 제작사: 애플 TV 영화 출력 
    path('appletv/', views.appletv, name = 'appletv')    
]
