
from turtle import title
from django.db import models

# Create your models here.

class tmdb_movie(models.Model):
    adult = models.CharField(max_length=20)
    backdrop_path = models.ImageField()
    genre_ids = models.IntegerField()
    id = models.IntegerField()
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.ImageField()
    release_date = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    video = models.AutoField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self):
        return (f"{self.id}번 : {self.title}")