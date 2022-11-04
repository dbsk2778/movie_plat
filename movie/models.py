from django.conf import settings 
from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.IntegerField()
    released_date = models.TextField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')

