from django.contrib.auth import forms as auth_forms
from django import forms


class CustomUserCreationForm(auth_forms.UserCreationForm):
    """내장 폼 클래스인 UserCreationForm 클래스를 상속받아 구현한 사용자 정의 폼 클래스."""

    # 기본적으로 제공하는 필드 외 추가로 입력받고 싶은 필드가 있으면 이곳에 작성.
    email = forms.CharField(max_length=100, label='이메일')  # 이메일 필드.
    address = forms.CharField(max_length=100, label='주소')  # 주소 필드.
