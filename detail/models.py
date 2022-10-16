from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from katalog.models import Toko

# Create your models here.
class JadwalOperasi(models.Model):
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    hari = models.CharField(max_length=8)
    jam_buka = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(24),
        ]
    )
    jam_tutup = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(24),
        ]
    )


class Barang(models.Model):
    class JenisBarang(models.TextChoices):
        makanan = "makanan"
        minuman = "minuman"
        pakaian = "pakaian"
        alat_tulis = "alat_tulis"

    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    harga = models.IntegerField(validators=[MinValueValidator(0)])
    deskripsi = models.TextField()
    jenis = models.CharField(max_length=16, choices=JenisBarang.choices)
