from django.shortcuts import redirect, render
from detail.models import Barang
from katalog.models import Toko
from detail.models import JadwalOperasi
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from dashboard.forms import TambahBarangForm
# Create your views here.

def show_dashboard(request):
    try:
        # toko = Toko.objects.get(pk = request.user.pk)
        tokoUser = Toko.objects.get(pk = 3)
        jadwal = JadwalOperasi.objects.filter(toko = tokoUser)
    except:
        tokoUser = None
    finally:
        context = {
            'toko' : tokoUser,
            'jadwal' : jadwal,
            'nama_pengguna' : request.user.username
        }
        return render(request, 'dashboard.html', context)

def show_data_json(request):
    data_toko = Toko.objects.filter(pk = 3)
    return HttpResponse(serializers.serialize("json", data_toko))

def show_barang_json(request):
    data_barang = Barang.objects.filter(toko = 3)
    return HttpResponse(serializers.serialize("json", data_barang))

def buka_tutup_toko(request):
    toko = Toko.objects.get(pk = 3)
    if(request.POST):
        if(toko.buka):
            toko.buka = False
        else:
            toko.buka = True
        toko.save()
        return redirect('dashboard:show_dashboard')
    return HttpResponseNotFound()

# def tambah_barang(request):
#     submitted = False
#     if(request.POST):
#         form = TambahBarangForm(request.POST)
#         if (form.is_valid()):
#             print("hello world")
#             barang = form.save(commit=False)
#             barang.toko = 3
#             barang.save()
#             return HttpResponse(b"CREATED", status = 201)
#         else:
#             form = TambahBarangForm
#             if 'submitted' in request.GET:
#                 submitted = True
#     return HttpResponseNotFound()

def quick_add_Barang(request):
    if(request.POST):
        nama_barang = request.POST.get('nama')
        harga_barang = request.POST.get('harga')
        jenis_barang = request.POST.get('jenis')
        desc_barang = request.POST.get('deskripsi')
        toko_barang = Toko.objects.get(pk = 3)

        new_task = Barang(nama = nama_barang, harga = harga_barang, jenis = jenis_barang, 
        deskripsi = desc_barang, toko = toko_barang)
        new_task.save()
        return HttpResponse(b"CREATED", status = 201)
    return HttpResponseNotFound()