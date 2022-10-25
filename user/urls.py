from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

app_name = 'user'
urlpatterns = [
    # 회원가입 페이지로 이동하거나 회원가입 처리를 하는 뷰
    # 내장 뷰 클래스인 CreateView 클래스를 상속하여 구현한 사용자 정의 뷰 클래스를 사용
    path('signup/', views.signup, name='signup'),
]