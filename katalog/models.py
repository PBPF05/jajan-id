from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Toko(models.Model):
    class HargaToko(models.TextChoices):
        mahal = "mahal"
        sedang = "sedang"
        murah = "murah"

    class KondisiToko(models.TextChoices):
        ramai = "ramai"
        sedang = "sedang"
        sepi = "sepi"

    nama = models.CharField(max_length=128)
    kota = models.CharField(max_length=64)
    provinsi = models.CharField(max_length=64)
    lokasi = models.CharField(max_length=128)
    deskripsi = models.TextField()
    range_harga = models.CharField(max_length=6, choices=HargaToko.choices)
    buka = models.BooleanField(default=True)
    kondisi = models.CharField(max_length=6, choices=KondisiToko.choices)
    pemilik = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
