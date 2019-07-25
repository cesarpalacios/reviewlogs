from django.db import models

class Person(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombr = models.CharField(max_length=30)

