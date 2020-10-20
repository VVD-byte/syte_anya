from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class clothes(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField(null = True)
    text = models.TextField(null = True)
    rasmer = models.CharField(max_length = 150)
    image1 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image2 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image3 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image4 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)

class game(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField(null = True)
    text = models.TextField(null = True)
    image1 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image2 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image3 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)
    image4 = models.ImageField(upload_to = 'user_images', height_field = None, width_field = None, max_length = None, blank = True)

class top(models.Model):
    name = models.CharField(max_length=100)