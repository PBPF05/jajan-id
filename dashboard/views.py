from django.shortcuts import render
from detail.models import Barang
from katalog.models import Toko
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
from dashboard.forms import TambahBarangForm
# Create your views here.

def show_dashboard(request):
    try:
        toko = Toko.objects.get(pk = request.user.pk)
    except:
        toko = None
    finally:
        context = {
            'toko' : toko,
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
    buka = request.POST.get('buka', None)
    toko.buka = buka
    toko.save()
    return HttpResponse(b"CREATED", status = 201)

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

# def quick_add_Barang(request):
#     if(request.POST):
#         nama_barang = request.POST.get('nama')
#         harga_barang = request.POST.get('harga')
#         jenis_barang = request.POST.get('jenis')
#         desc_barang = request.POST.get('deskripsi')
#         toko_barang = request.GET.get('toko')

#         new_task = Barang(nama = nama_barang, harga = harga_barang, jenis = jenis_barang, deskripsi = desc_barang, toko = toko_barang)
#         new_task.save()
#         return HttpResponse(b"CREATED", status = 201)
#     return HttpResponseNotFound()