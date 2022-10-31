# 네이버 영화 검색 API 
# https://developers.naver.com/docs/serviceapi/search/movie/movie.md#%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C
# https://colab.research.google.com/ 실행 (주피터 노트북)
import os
import sys
from doctest import debug_script
import urllib.request 
import pandas as pd
import json
import re


client_id = "QNw9k2mLukjBHx1zWHsG"
client_secret = "GvPiAz3U6C"

# 실행 : ctrl + F5
# 검색 키워드 (pasre.quote : utf8 변경)
# 결과 JSON 값으로 출력, key + value
query = urllib.parse.quote(input("검색어: "))
# encText = urllib.parse.quote("컴퓨터")


# 인덱스 1000개까지 불러오도록 설정
idx = 0 
# 네이버 API 기본 10개까지 보여줌, 100개 단위로 가져오도록 설정
display = 100
start = 1
end = 1000
sort = "sim"
# data print 값으로 불러오는 게 아니라, pandas 사용해서 불러오기
# pandas DataFrame : 테이블 형식의 데이터를 다룰 때 사용(열 8개의 데이터프레임 완성)
movie_df = pd.DataFrame(columns=('Title', 'Link', 'Image', 'Subtitle', 'Publication Date', 'Director', 'Actor','User Rating'))

# 1부터 1000까지, 100개 단위(100개씩 가져와야 하니까)
for start_index in range(start, end, display):

    # JSON 결과, 시작 위치가 계속 바뀌면서 출력 가능
    url = "https://openapi.naver.com/v1/search/movie?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index) \
        + "&sort=" + sort


    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    # rescode==200, 성공 의미, API 요청 응답을 받았다는 의미(정상적인 응답)
    if(rescode==200):
        response_body = response.read()
        # 파싱
        response_dict = json.loads(response_body.decode('utf-8'))
        # items 안의 값을 가져와야 하므로, items 키에 해당하는 거 다 가져옴 
        items = response_dict['items']

        for item_index in range(0, len(items)):
            # 결과값에 <b>검색어</b> 태그 설정되어 있으므로 태그 삭제하기 위한 re 모듈 import
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, "", items[item_index]['title'])
            link = items[item_index]['link']
            image = items[item_index]['image']
            subtitle = items[item_index]['subtitle']
            pub_date = items[item_index]['pubDate']
            director = items[item_index]['director']
            actor = items[item_index]['actor']
            user_rating = items[item_index]['userRating']

            # 만들어놓은 데이터프레임에 넣어주기
            movie_df.loc[idx] = [title, link, image, subtitle, pub_date, director, actor, user_rating]
            idx += 1  # index 값 +1 씩 증가
    else:
        print("Error Code:" + rescode)

# 주피터에서는 print 함수 안쓰고 movie_df라고만 해도 출력됨
# 여기서는 왜 출력 안되는건지 찾아보기
print(movie_df) 

# 데이터프레임 csv(엑셀) 파일로 저장 : 글자 깨짐(인코딩 설정)
# 이미 searchapi.csv 파일 있으면 파일 저장 안됨, 파일 저장 후 삭제 어떻게?
movie_df.to_csv('C:\Workspace\searchapi.csv', encoding='euc-kr') #csv파일로 생성


