from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20, blank=True, default="0.0.0")
    url = models.CharField(max_length=200)
