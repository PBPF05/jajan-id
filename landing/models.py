from django.db import models

# Create your models here.
class Kontak(models.Model):
    email = models.CharField(max_length=64)
    pesan = models.TextField()