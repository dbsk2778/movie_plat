from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

app_name = 'user'
urlpatterns = [
    # 회원가입 페이지로 이동하거나 회원가입 처리를 하는 뷰(아름1025)
    path('signup/', views.signup, name='signup'),

    # 로그아웃 처리를 하는 뷰.
    # next_page: 로그아웃 처리 후 리다이렉트할 URL 값. 기본 값은 None(아름1025)
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]