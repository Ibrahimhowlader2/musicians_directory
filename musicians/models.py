from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Violin', 'Violin'),
        ('Drums', 'Drums'),
        ('Saxophone', 'Saxophone'),
    ]
    instrument_type = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
