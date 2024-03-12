from django.db import models

# Create your models here.
class Recipe(models.Model):
    picture = models.ImageField(null = True, blank = True, upload_to = "recipe_images/")
    name = models.CharField(max_length = 200)
    description = models.TextField()
    category = models.CharField(max_length = 200)
    process = models.CharField(max_length = 200)
    ingredients = models.CharField(max_length = 300)
