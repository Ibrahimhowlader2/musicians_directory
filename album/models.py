from django.db import models
from musicians.models import Musician
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date=models.DateTimeField(auto_now_add=True)
    RATING_CHOICES=( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ) 
    ratings = models.CharField(choices=RATING_CHOICES, max_length=1, default='4')
    def __str__(self):
        return self.album_name

