from django.db import models


class Translate(models.Model):
    name = models.CharField(max_length=100)
    translate = models.CharField(max_length=100)
