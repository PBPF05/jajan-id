from typing import TYPE_CHECKING
from django.db import models
from katalog.models import Toko
from django.contrib.auth.models import User

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class Channel(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["toko", "user"],
                name="toko_user_uq",
            )
        ]
        indexes = [models.Index(fields=["toko", "user"], name="toko_user_idx")]

    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    pesan_set: "RelatedManager[Pesan]"


class Pesan(models.Model):
    class Pengirim(models.TextChoices):
        pengirim = "pengirim"
        user = "user"

    pesan = models.CharField(max_length=256)
    pengirim = models.CharField(max_length=8, choices=Pengirim.choices)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
