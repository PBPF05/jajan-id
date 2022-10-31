from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from detail.models import JadwalOperasi
from detail.models import Barang
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# @login_required(login_url="../login")
def detail_toko(request):
    data_jam = JadwalOperasi.objects.all()
    # (user = request.user)
    data_barang = Barang.objects.all()
    # (user = request.user)
    context = {
        'detail.jadwaloperasi' : data_jam,
        'detail.barang' : data_barang,
    }
    return render(request, 'detail.html', context)

def detail_json(request):
    data_jam = JadwalOperasi.objects.all() 
    # (user = request.user)
    data_barang = Barang.objects.all() 
    # (user = request.user)
    return HttpResponse(serializers.serialize("json", data_jam, data_barang), content_type="application/json")

@csrf_exempt
def jam(request):
    if request.method == 'POST':
        toko = request.POST.get('toko')
        hari = request.POST.get('hari')
        jam_buka = request.POST.get('jam_buka')
        jam_tutup = request.POST.get('jam_tutup')
        jam = JadwalOperasi.objects.create(
            toko = toko, 
            hari = hari,
            jam_buka = jam_buka,
            jam_tutup = jam_tutup,
            user = request.user)
        return JsonResponse(
            {
                "pk": jam.pk,
                "fields": {
                    "toko": jam.toko,
                    "hari": jam.hari,
                    "jam_buka": jam.jam_buka,
                    "jam_tutup": jam.jam_tutup,
                },
            },
        )
    return HttpResponseBadRequest()

@csrf_exempt
def barang(request):
    if request.method == 'POST':
        toko = request.POST.get('toko')
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')
        jenis = request.POST.get('jenis')
        item = Barang.objects.create(
            toko = toko, 
            nama = nama,
            harga = harga,
            deskripsi = deskripsi,
            jenis = jenis, 
            user = request.user)
        return JsonResponse(
            {
                "pk": item.pk,
                "fields": {
                    "nama": item.nama,
                    "harga": item.harga,
                    "deskripsi": item.deskripsi,
                    "jenis": item.jenis,
                },
            },
        )
    return HttpResponseBadRequest()

# @login_required(login_url='.../login/')
# def review(request):
#     if request.method == "POST":
#         form = reviewform(request.POST)
#         form.instance.user = request.user
#         if form.is_valid():
#             form.save()
#             response = HttpResponseRedirect(reverse("detail:detail_toko"))
#             return response
#     else:
#         form = reviewform()
#     return render(request, "review.html")