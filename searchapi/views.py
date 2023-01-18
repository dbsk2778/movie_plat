# 전달받은 정보에 필요한 데이터를 모듈에게 달라고 요청
import json
import urllib.request
from django.shortcuts import render
# from sqlalchemy import create_engine


def search(request):
    if request.method == 'GET':

        client_id = "QNw9k2mLukjBHx1zWHsG"
        client_secret = "GvPiAz3U6C"

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        idx = 0 
        # 네이버 API 기본 10개까지 보여줌, 100개 단위로 가져오도록 설정
        display = 100
        start = 1
        end = 1000
        sort = "sim"

        for start_index in range(start, end, display):
            url = "https://openapi.naver.com/v1/search/movie?query=" + encText \
            + "&display=" + str(display) \
            + "&start=" + str(start_index) \
            + "&sort=" + sort

            movie_api_request = urllib.request.Request(url)
            movie_api_request.add_header("X-Naver-Client-Id", client_id)
            movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(movie_api_request)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = response.read()
                result = json.loads(response_body.decode('utf-8'))
                items = result.get('items')
                # print(result) 

                context = {
                    'items': items
                }


            else:
                print("Error Code:" + rescode)
            
            return render(request, 'search/search.html', context=context)
    
 

 