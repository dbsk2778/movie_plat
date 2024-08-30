from django.contrib import messages
from django.contrib.auth import models, forms, logout, update_session_auth_hash
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm, CheckPasswordForm
from .decorators import login_message_required
from .forms import CustomUserCreationForm
from movie.models import Like


# 로그인
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



# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('/')



# 프로필 보기
@login_message_required
def profile_view(request):
    
    if request.method == 'GET':
        likes = Like.objects.filter(username=request.user.id)
        context = {
            'likes': likes
        }

    return render(request, 'user/profile.html', context)


# 프로필 수정
@login_message_required
def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'user/profile.html')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)

        return render(request, 'user/profile_update.html', {'user_change_form':user_change_form})


# 회원탈퇴
@login_message_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'user/profile_delete.html', {'password_form':password_form})

