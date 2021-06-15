from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=70)
    genres=models.CharField(max_length=70)
    year=models.CharField(max_length=70)
    image=models.ImageField(upload_to="movie_image")
    movieduration=models.CharField(max_length=70)
    def __str__(self):
        return str(self.pk)

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,default=None)
    rating=models.CharField(max_length=70)
    rated_date=models.DateTimeField(auto_now_add=True)

