from django.shortcuts import render
from .models import Movie
import json
import requests


my_api_key = '0e8214551d621b3afb24dfa745c02cfa'

def movie_data(request):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=0e8214551d621b3afb24dfa745c02cfa&language=ko-KR&page=1'
    response = requests.get(url)
    #response 객체 안에는 우리가 보낸 url의 응답 객체 그 자체

    resdata = response.text
    # 응답 객체 그 자체를 가공해 정보로 만든 것이 .text
    
    obj = json.loads(resdata)
    # python에서는 python객체를 사용해야하기때문에 json을 import한 후 python 객체로 가공해 담아준다.
    
    # json formatter를 이용해 result만 담은 obj 생성
    obj = obj['results']
    return render(request, 'common/home.html', {'obj':obj})


def genre(request):
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=0e8214551d621b3afb24dfa745c02cfa&language=ko-KR'
    response = requests.get(url)
    #response 객체 안에는 우리가 보낸 url의 응답 객체 그 자체

    resdata = response.text
    # 응답 객체 그 자체를 가공해 정보로 만든 것이 .text
    
    obj = json.loads(resdata)
    # python에서는 python객체를 사용해야하기때문에 json을 import한 후 python 객체로 가공해 담아준다.
    
    # json formatter를 이용해 result만 담은 obj 생성
    obj = obj['genres']
    return render(request, 'movie.html', {'obj':obj})


def detail(request):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0e8214551d621b3afb24dfa745c02cfa&language=ko-KR'
    response = requests.get(url)
    #response 객체 안에는 우리가 보낸 url의 응답 객체 그 자체
    resdata = response.text
    # 응답 객체 그 자체를 가공해 정보로 만든 것이 .text
    obj = json.loads(resdata)
    # python에서는 python객체를 사용해야하기때문에 json을 import한 후 python 객체로 가공해 담아준다.
    
    # json formatter를 이용해 result만 담은 obj 생성

    obj = obj['genres']

    return render(request, 'detail.html', {'obj':obj})