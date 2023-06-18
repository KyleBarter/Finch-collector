from typing import Type
from django.db import models
from django.db.models.options import Options
from django.urls import reverse

MEALS = (
    ('B', 'breakfast'),
    ('L', 'lunch'),
    ('D', 'dinner'),
)

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.color}, {self.species}, {self.location}, ({self.id})'
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'finch_id' : self.id})
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    #create a finch_id FK 
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta():
        ordering = ["-date"]