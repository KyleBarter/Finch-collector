from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.color}, {self.species}, {self.location}, ({self.id})'
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'finch_id' : self.id})