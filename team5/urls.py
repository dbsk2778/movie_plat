"""team5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views import generic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.TemplateView.as_view(template_name='common/dist/welcome.html'), name='welcome'),
    path('user/', include('user.urls')),
    path('home/', generic.TemplateView.as_view(template_name='common/home.html'), name='home'),
    # searchapi 앱의 url 파일
    path('searchapi/', include('searchapi.urls')),
    # path('searchapi/', include('searchapi.urls')),
    path('choice/', generic.TemplateView.as_view(template_name='user/choice.html'), name='choice'),
    path('movie/', include('movie.urls')),

    # 소셜 로그인 관련
    path('accounts/', include('allauth.urls')),
]
