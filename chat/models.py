from django.db import models
from katalog.models import Toko
from django.contrib.auth.models import User

# Create your models here.
class Pesan(models.Model):
    class Pengirim(models.TextChoices):
        pengirim = "pengirim"
        user = "user"

    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pesan = models.CharField(max_length=256)
    pengirim = models.CharField(max_length=8, choices=Pengirim.choices)
