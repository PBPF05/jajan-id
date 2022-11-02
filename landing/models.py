from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kontak(models.Model):
    pesan = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_seller = models.BooleanField(default=False)
    