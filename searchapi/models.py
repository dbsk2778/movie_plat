# 데이터베이스에서 해당 정보를 가져와서 번역한 뒤
# 다시 views.py에 전달
# views.py는 manage한테 가져온 정보와 프론트에게 전달받은 정보를 
# 믹싱하여 templates, html로 프론트엔드로 보냄

from django.db import models

# 데이터베이스 안의 데이터는 엑셀의 테이블형식(행, 열)으로 데이터가 들어가게 되는데
# models.py에서 클래스를 정의하여 서로 매칭되면서 데이터 교류

class Searchapi(models.Model):

    # 'Title', 'Link', 'Image', 'Subtitle', 'Publication Date', 
    # 'Director', 'Actor','User Rating' 
    # 테이블 생성, 데이터 타입 확인 * 

    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    subtitle = models.TextField(db_column='Subtitle', blank=True, null=True)  # Field name made lowercase.
    pub_date = models.TextField(db_column='Publication Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.     
    director = models.TextField(db_column='Director', blank=True, null=True)  # Field name made lowercase.
    actor = models.TextField(db_column='Actor', blank=True, null=True)  # Field name made lowercase.
    user_rating = models.TextField(db_column='User Rating', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        # 테이블 이름을 searchmovie로 변경
        # 모델이 참조하는 테이블 이름
        db_table = 'search_movie'