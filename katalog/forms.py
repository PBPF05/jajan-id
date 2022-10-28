from katalog.models import Toko
from django import forms
from django.forms import ModelForm

class katalogforms(ModelForm):
    class Meta:
        model = Toko
        fields = ('nama', 'kota', 'provinsi', 'lokasi', 'deskripsi', 'range_harga', 'buka', 'kondisi')
