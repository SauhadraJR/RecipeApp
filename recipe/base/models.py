from django.db import models

# Create your models here.
class Recipe(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length = 200)
    description = models.TextField()
    category = models.CharField(max_length = 200)
    process = models.CharField(max_length = 200)
    ingredients = models.CharField(max_length = 300)
