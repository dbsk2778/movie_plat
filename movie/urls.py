from django.urls import path
from . import views


app_name = 'movie'
urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('choice/', views.choice, name='choice'),
]

