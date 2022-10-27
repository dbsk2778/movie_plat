
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# 회원가입 (아름1025)
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username = request.POST['username'],
                                            email = request.POST['email'],
                                            password = request.POST['password1'],
                                            )
            auth.login(request, user)
            return redirect('/')
    return render(request, 'user/signup.html')

# 로그인 (아름)
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error' : 'email or passeord is incorrect.'})
    else:
        return render(request, 'user/login.html')

