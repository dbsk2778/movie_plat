DATABASES = {
    'default': {
        # engine 기능 : 장고가 자동으로 데이터베이스 언어 번역해서 넘겨줌
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'mymovie',
        'USER' : 'director',
        # 'USER' : 'root',
        'PASSWORD' : '1234',
        # 'HOST' : '192.168.245.68',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}

