from django.shortcuts import render
from detail.models import Barang
from katalog.models import Toko
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
from dashboard.forms import TambahBarangForm
# Create your views here.

def show_dashboard(request):
    toko = Toko.objects.filter(pk = 3)
    return render(request, 'dashboard.html')

def show_data_json(request):
    data_toko = Toko.objects.filter(pk = 3)
    return HttpResponse(serializers.serialize("json", data_toko))

def show_barang_json(request):
    data_barang = Barang.objects.filter(toko = 3)
    return HttpResponse(serializers.serialize("json", data_barang))

def buka_tutup_toko(request):
    toko = Toko.objects.filter(pk = 3)
    buka = request.GET.get('buka', None)
    toko.buka = buka
    toko.save()
    return HttpResponse(b"CREATED", status = 201)

def tambah_barang(request):
    submitted = False
    if(request.POST):
        form = TambahBarangForm(request.POST)
        if (form.is_valid()):
            barang = form.save(commit=False)
            barang.toko = request.user.pk
            barang.save()
            return HttpResponse(b"CREATED", status = 201)
        else:
            form = TambahBarangForm
            if 'submitted' in request.GET:
                submitted = True
    return HttpResponseNotFound()