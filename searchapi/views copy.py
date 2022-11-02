# 전달받은 정보에 필요한 데이터를 모듈에게 달라고 요청
import json
import urllib.request
import pandas as pd
import re

from django.shortcuts import render
from django.http import HttpResponse

from sqlalchemy import create_engine
import pymysql

from django.db import connection

from .models import Searchapi

# ipconfig 주소 설정
engine = create_engine("mysql+pymysql://director:1234@127.0.0.1:3306/mymovie")
# engine = create_engine("mysql+pymysql://director:1234@172.30.1.32:3306/mymovie")
conn = engine.connect

# client_id = "QNw9k2mLukjBHx1zWHsG"
# client_secret = "GvPiAz3U6C"


def search(request):
    if request.method == 'GET':

        client_id = "QNw9k2mLukjBHx1zWHsG"
        client_secret = "GvPiAz3U6C"
        
        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            print(result)  # request를 예쁘게 출력해볼 수 있다.

            context = {
                'items': items
            }
        else:
            print("Error Code:" + rescode)
        
        
        return render(request, 'search/search.html', context=context)

 