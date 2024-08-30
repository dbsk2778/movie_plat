from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import check_password
from django import forms
from django.contrib.auth import get_user_model



class CustomUserCreationForm(auth_forms.UserCreationForm):
    """내장 폼 클래스인 UserCreationForm 클래스를 상속받아 구현한 사용자 정의 폼 클래스."""

    # 기본적으로 제공하는 필드 외 추가로 입력받고 싶은 필드가 있으면 이곳에 작성.
    email = forms.CharField(max_length=100, label='이메일')  # 이메일 필드.


# 회원정보 수정 폼
class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(max_length=10, label='아이디')
    password = None            
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(
        attrs={'class': 'form-control',}), 
    )   
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']


# 회원탈퇴 비밀번호 확인 폼
class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')