import imp
from django import forms
from detail.models import Barang

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