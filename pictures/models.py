from django.db import models

# Create your models here.
class Pictures(models.Model):
    picture = models.TextField(default="picture")
    description = models.TextField(default = "this is a picture")
    location = models.TextField(default = "here")
