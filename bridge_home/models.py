from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.TextField()
    description = models.TextField()
    active = models.TextField(default = "this is true")
    