from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'user'
urlpatterns = [
    # 회원가입 페이지로 이동하거나, 회원가입 처리를 하는 뷰.
    # 내장 뷰 클래스인 CreateView 클래스를 상속하여 구현한 사용자 정의 뷰 클래스를 사용.
    path('signup/', views.UserCreateView.as_view(), name='signup'),

    # 로그인 페이지로 이동하거나, 로그인 처리를 하는 뷰.
    # 내장 뷰 클래스인 LoginView 클래스를 사용.
    # as_view() 함수에 다음과 같은 인수를 추가하여 설정을 변경할 수 있다.
    # # template_name: GET 요청 시 응답할 템플릿 파일 이름. 기본 값은 'registration/login.html'.
    # # next_page: POST 요청 시 리다이렉트할 URL 값. 기본 값은 '/accounts/profile/'.
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html',
        next_page='movie:choice'
    ), name='login'),

    # 로그아웃 처리를 하는 뷰.
    # as_view() 함수에 다음과 같은 인수를 추가하여 설정을 변경할 수 있다.
    # # template_name: 로그아웃 처리 후 응답할 템플릿 파일 이름. 기본 값은 'registration/logged_out.html'.
    # # next_page: 로그아웃 처리 후 리다이렉트할 URL 값. 기본 값은 None.
    path('logout/', auth_views.LogoutView.as_view(
        # template_name='user/user_form.html',
        next_page='/'
    ), name='logout'),

    
    # 유저 프로필
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),


]
