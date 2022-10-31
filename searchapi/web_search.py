# 네이버 웹문서 검색 API 

import os
import sys
from doctest import debug_script
import urllib.request 
import pandas as pd
import json
import re


client_id = "QNw9k2mLukjBHx1zWHsG"
client_secret = "GvPiAz3U6C"

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
# data print 값으로 불러오는 게 아니라, pandas 사용해서 불러오기
# pandas DataFrame : 테이블 형식의 데이터를 다룰 때 사용(열 3개의 데이터프레임 완성)
web_df = pd.DataFrame(columns=('Title', 'Link', 'Description'))

# 1부터 1000까지, 100개 단위(100개씩 가져와야 하니까)
for start_index in range(start, end, display):

    # JSON 결과, 시작 위치가 계속 바뀌면서 출력 가능
    url = "https://openapi.naver.com/v1/search/blog?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index)


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
            description = re.sub(remove_tag, "", items[item_index]['description'])
            # 만들어놓은 데이터프레임에 넣어주기
            web_df.loc[idx] = [title, link, description]
            idx += 1  # index 값 +1 씩 증가
    else:
        print("Error Code:" + rescode)

print(web_df)  # 데이터프레임 출력

    