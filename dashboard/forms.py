import imp
from django import forms
from detail.models import Barang
from katalog.models import Toko

class BuatTokoForm(forms.ModelForm):
    class Meta:
        model = Toko
        fields = ('nama', 'kota', 'provinsi', 'lokasi', 'deskripsi', 'range_harga', 'kondisi')

        widgets = {
            'nama' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'ex: Seblak Bandung Seuhah', 'class' : 'form-control'}),
            'kota' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'ex: Depok', 'class' : 'form-control'}),
            'provinsi' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'ex: Jawa Barat', 'class' : 'form-control'}),
            'lokasi' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'ex: Jl. Akses UI', 'class' : 'form-control'}),
            'deskripsi' : forms.Textarea(attrs={'type' : 'textarea', 'placeholder' : 'Deskripsi', 'class' : 'form-control'}),
            'range_harga' : forms.Select(choices=Toko.HargaToko),
            'kondisi' : forms.Select(choices=Toko.KondisiToko)
        }

        nama = forms.CharField(label = 'Nama', required = True, widget = widgets['nama'])
        kota = forms.CharField(label = 'Kota', required = True, widget = widgets['kota'])
        provinsi = forms.CharField(label = 'Provinsi', required = True, widget = widgets['provinsi'])
        lokasi = forms.CharField(label = 'Lokasi', required = True, widget = widgets['lokasi'])
        deskripsi = forms.CharField(label = 'Deskripsi', required = True, widget = widgets['deskripsi'])
        range_harga = forms.CharField(label = 'Range Harga', required = True, widget = widgets['range_harga'])
        kondisi = forms.CharField(label = 'Kondisi', required = True, widget = widgets['kondisi'])
