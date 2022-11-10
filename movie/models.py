from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.TextField(default='0')

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre)
    

class Usergenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
