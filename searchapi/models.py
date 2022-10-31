# 데이터베이스에서 해당 정보를 가져와서 번역한 뒤
# 다시 views.py에 전달
# views.py는 manage한테 가져온 정보와 프론트에게 전달받은 정보를 
# 믹싱하여 templates, html로 프론트엔드로 보냄

from django.db import models

# 데이터베이스 안의 데이터는 엑셀의 테이블형식(행, 열)으로 데이터가 들어가게 되는데
# models.py에서 클래스를 정의하여 서로 매칭되면서 데이터 교류

# class Searchapi(models.Model):

#     # 'Title', 'Link', 'Image', 'Subtitle', 'Publication Date', 
#     # 'Director', 'Actor','User Rating'
#     # 테이블 생성, 데이터 타입 확인 * 

#     title = models.CharField(max_length=100)
#     link = models.CharField(max_length=1000)
#     image = models.CharField(max_length=1000)
#     subtitle = models.CharField(max_length=1000)
#     pub_date = models.CharField(max_length=100)
#     director = models.CharField(max_length=100)
#     actor = models.CharField(max_length=100)
#     user_rating = models.CharField(max_length=1000)

#     class Meta:
#         db_table = 'searchmovie'

