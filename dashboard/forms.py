import imp
from django import forms
from detail.models import Barang
from katalog.models import Toko

# class updateDataForms(forms.ModelForm):
class TambahBarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ('nama', 'harga', 'jenis', 'deskripsi')

        widgets = {
            # 'date' : forms.DateInput(),
            'nama' : forms.TextInput(attrs={'type' : 'text', 'placeholder' : 'ex: Cimol', 'class' : 'form-control'}),
            'harga' : forms.NumberInput(attrs={'type' : 'text', 'placeholder' : 'ex: 20000', 'class' : 'form-control'}),
            'jenis' : forms.Select(choices=Barang.JenisBarang),
            'deskripsi' : forms.Textarea(attrs={'type' : 'textarea', 'placeholder' : 'Deskripsi', 'class' : 'form-control'})
            }

        nama = forms.CharField(label = 'Nama', required = True, widget = widgets['nama'])
        harga = forms.IntegerField(label = 'Harga', required = True, widget = widgets['harga'])
        jenis = forms.CharField(label = 'Jenis', required = True, widget=widgets['jenis'])
        deskripsi = forms.CharField(label = 'Deskripsi', required = True, widget = widgets['deskripsi'])

class BuatTokoFrom(forms.ModelForm):
    class Meta:
        model = Toko
        fields = ('nama', 'kota', 'provinsi', 'lokasi', 'deskripsi', 'range_harga', )

    #     nama = models.CharField(max_length=128)
    # kota = models.CharField(max_length=64)
    # provinsi = models.CharField(max_length=64)
    # lokasi = models.CharField(max_length=128)
    # deskripsi = models.TextField()
    # range_harga = models.CharField(max_length=6, choices=HargaToko.choices)
    # buka = models.BooleanField(default=True)
    # kondisi = models.CharField(max_length=6, choices=KondisiToko.choices)
    # pemilik = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)