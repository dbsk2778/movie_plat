from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('choice/', views.genre, name='choice'),
    path('usergenre/', views.usergenre, name='usergenre'),
    path('recommand/',views.recommand, name='recommand')

]
