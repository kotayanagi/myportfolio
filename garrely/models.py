from django.db import models


class Photo(models.Model):

    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=30)
    camera = models.CharField(max_length=50)
    description = models.CharField(max_length=50)