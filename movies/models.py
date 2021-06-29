from django.db import models
from django.db.models.deletion import CASCADE

class Movie(models.Model):
    title = models.CharField(max_length = 100, blank=False)
    description = models.CharField(max_length = 1000, default='')
    year = models.SmallIntegerField(default=2000)
    director = models.CharField(max_length = 100, default='')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    review = models.CharField(max_length=2000, default='')
    rating = models.SmallIntegerField(default=5, blank=False)
    def __str__(self):
        return self.review