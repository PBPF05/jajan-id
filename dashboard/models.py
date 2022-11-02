from django.db import models
from django.contrib.auth.models import User
from katalog.models import Toko
# Create your models here.
class Review:
    komentator = models.ForeignKey(User, on_delete = models.CASCADE)
    komentar = models.TextField()
    toko = models.ForeignKey(Toko, on_delete = models.CASCADE)