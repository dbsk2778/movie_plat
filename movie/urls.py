from django.urls import path

from . import views


urlpatterns = [
    path('movie/', views.movie_data, name='movie'),
    path('detail/<str:movie_id>', views.detail),
]