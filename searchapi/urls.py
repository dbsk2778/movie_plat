# 프론트엔드로부터 정보를 전달받아 
# 해당하는 담당 views.py에 연결
# url > views > models > views

from django.conf.urls import url, path
from . import views
# from searchapi import views

app_name='searchapi'

urlpatterns = [
    url('searchapi/', views.search, name='search_api')
]
