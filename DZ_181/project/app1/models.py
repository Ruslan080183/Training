from django.db import models

class Genre(models.Model):

    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Film(models.Model):

    title = models.CharField(max_length=300)
    country = models.CharField(max_length=200)
    year = models.IntegerField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.title} {self.country} {self.year}"
class Viewer(models.Model):
    name = models.CharField(max_length=300)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    def __str__(self):
        return F"{self.name} {self.film}"
class RatingViews(models.Model):
    views = models.IntegerField(max_length=100)
