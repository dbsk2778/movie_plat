from audioop import reverse
from django.contrib.auth import models, forms
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render


class UserCreateView(generic.CreateView):
    """
    내장 뷰 클래스인 CreateView를 상속하여 구현한 사용자 정의 CreateView.
    GET 요청 시 회원가입 페이지로 이동하고,
    POST 요청 시 내장 모델 클래스인 User를 사용하여 회원가입 처리를 한다.
    """
    # form_class 변수를 통해 일괄 설정하는 경우.
    form_class = forms.UserCreationForm
    template_name = 'user/signup.html'  # GET 요청을 처리할 때 응답할 템플릿 파일.
    success_url = reverse_lazy('user:login')  # POST 요청을 처리할 때 리다이렉트할 URL.
