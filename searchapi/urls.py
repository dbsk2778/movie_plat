# 프론트엔드로부터 정보를 전달받아 
# 해당하는 담당 views.py에 연결
# url > views > models > views

# from django.conf.urls import url
from django.urls import path
from . import views
from django.urls import re_path as url 
# from searchapi import views

app_name='searchapi'

urlpatterns = [
    # name = 별칭, url> path로 고치면 에러? 확인?
    url('search/', views.search, name='search_api'),
    url('searchdata/', views.searchData, name='search_data'),
]
