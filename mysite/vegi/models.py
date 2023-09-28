from django.db import models
from django.utils import timezone

# Create your models here.


class receipes(models.Model):
    
    recipe_name = models.CharField(max_length = 100)

    recipe_desc = models.TextField()

    recipe_image = models.ImageField( upload_to= 'recipe' ,default=timezone.now )


