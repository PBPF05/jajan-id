from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from detail.models import Barang
from katalog.models import Toko
from detail.models import JadwalOperasi
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from dashboard.forms import BuatTokoForm
# Create your views here.

@login_required(login_url='/login/')
def show_dashboard(request):
    try:
        tokoUser = Toko.objects.get(pk = request.user.pk)
        # tokoUser = Toko.objects.get(pk = 3)
        jadwal = JadwalOperasi.objects.filter(toko = tokoUser)
    except:
        tokoUser = None
        jadwal = None
    finally:
        context = {
            'toko' : tokoUser,
            'jadwal' : jadwal,
            'nama_pengguna' : request.user.username
        }
        return render(request, 'dashboard.html', context)

def show_data_json(request):
    data_toko = Toko.objects.filter(pk = request.user.pk)
    # data_toko = Toko.objects.filter(pk = 3)
    return HttpResponse(serializers.serialize("json", data_toko))

def show_barang_json(request):
    data_toko = Toko.objects.get(pk = request.user.pk)
    # data_toko = Toko.objects.get(pk = 3)
    data_barang = Barang.objects.filter(toko = data_toko)
    return HttpResponse(serializers.serialize("json", data_barang))

def show_barang_json_byid(request, id):
    data_toko = Toko.objects.get(pk = request.user.pk)
    # data_toko = Toko.objects.get(pk = 3)
    data_barang = Barang.objects.filter(toko = data_toko).filter(pk = id)
    return HttpResponse(serializers.serialize("json", data_barang))

def show_jadwal_json(request):
    data_toko = Toko.objects.get(pk = request.user.pk)
    # data_toko = Toko.objects.get(pk = 3)
    data_barang = JadwalOperasi.objects.filter(toko = data_toko)
    return HttpResponse(serializers.serialize("json", data_barang))

def show_jadwal_json_byid(request, id):
    data_toko = Toko.objects.get(pk = request.user.pk)
    # data_toko = Toko.objects.get(pk = 3)
    data_barang = JadwalOperasi.objects.filter(toko = data_toko).filter(pk = id)
    return HttpResponse(serializers.serialize("json", data_barang))

def buka_tutup_toko(request):
    toko = Toko.objects.get(pk = request.user.pk)
    # toko = Toko.objects.get(pk = 3)
    if(request.POST):
        if(toko.buka):
            toko.buka = False
        else:
            toko.buka = True
        toko.save()
        return redirect('dashboard:show_dashboard')
    return HttpResponseNotFound()

def quick_add_Barang(request):
    if(request.POST):
        nama_barang = request.POST.get('inputNama')
        harga_barang = request.POST.get('inputHarga')
        jenis_barang = request.POST.get('inputJenis')
        desc_barang = request.POST.get('inputDeskripsi')
        toko_barang = Toko.objects.get(pk = request.user.pk)
        # toko_barang = Toko.objects.get(pk = 3)

        new_barang = Barang(nama = nama_barang, harga = harga_barang, jenis = jenis_barang, 
        deskripsi = desc_barang, toko = toko_barang)
        new_barang.save()
        return HttpResponse(b"CREATED", status = 201)
    return HttpResponseNotFound()

def delete_barang(request, id):
    context = {}
    task = get_object_or_404(Barang,pk = id)
    
    if(request.POST):
        task.delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()

def create_toko(request):
    user = request.user
    if(request.POST):
        form = BuatTokoForm(request.POST, instance=request.user)
        if form.is_valid:
            o = form.save(commit=False)
            o.pemilik = request.user
            o.save()
        return redirect('dashboard:show_dashboard')
    return render(request, 'create-toko.html', {'form' : BuatTokoForm})

def update_toko(request):
    nama_toko = request.POST.get('inputNama')
    kota_toko = request.POST.get('inputKota')
    provinsi_toko = request.POST.get('inputProvinsi')
    lokasi_toko = request.POST.get('inputLokasi')
    desc_barang = request.POST.get('inputDeskripsi')

    toko = Toko.objects.get(pk = request.user.pk)
    # toko = Toko.objects.get(pk = 3)
    toko.nama = nama_toko
    toko.kota = kota_toko
    toko.provinsi = provinsi_toko
    toko.lokasi = lokasi_toko
    toko.deskripsi = desc_barang
    toko.save()

    new_toko = {
        'nama': toko.nama, 
        'kota': toko.kota, 
        'provinsi': toko.provinsi,
        'lokasi':toko.lokasi,
        'deskripsi': toko.deskripsi
    }
    return HttpResponse(b"CREATED", status = 201)

def update_barang(request, id):
    nama_barang = request.POST.get('inputEditNama')
    harga_barang = request.POST.get('inputEditHarga')
    jenis_barang = request.POST.get('inputEditJenis')
    desc_barang = request.POST.get('inputEditDeskripsi')
    toko_barang = Toko.objects.get(pk = request.user.pk)
    # toko_barang = Toko.objects.get(pk = 3)

    barang = Barang.objects.filter(pk = id).get(toko = toko_barang)
    barang.nama = nama_barang
    barang.harga = harga_barang
    barang.jenis = jenis_barang
    barang.deskripsi = desc_barang
    barang.save()

    new_barang = {
        'pk': barang.pk,
        'nama': barang.nama, 
        'harga': barang.harga, 
        'jenis': barang.jenis,
        'deskripsi': barang.deskripsi
    }
    return HttpResponse(b"CREATED", status = 201)

def create_jadwal(request):
    if(request.POST):
        hari_buka = request.POST.get('inputHari')
        jam_buka_toko = request.POST.get('inputJamBuka')
        jam_tutup_toko = request.POST.get('inputJamTutup')
        toko_jadwal = Toko.objects.get(pk = request.user.pk)
        # toko_jadwal = Toko.objects.get(pk = 3)

        jadwal = JadwalOperasi(hari = hari_buka, jam_buka = jam_buka_toko, jam_tutup = jam_tutup_toko, toko = toko_jadwal)
        jadwal.save()
        return HttpResponse(b"CREATED", status = 201)
    return HttpResponseNotFound()

def update_jadwal(request, id):
    hari_buka = request.POST.get('inputEditHari')
    jam_buka_toko = request.POST.get('inputEditJamBuka')
    jam_tutup_toko = request.POST.get('inputEditJamTutup')
    toko_barang = Toko.objects.get(pk = request.user.pk)
    # toko_barang = Toko.objects.get(pk = 3)

    jadwal = JadwalOperasi.objects.filter(toko = toko_barang).get(pk=id)
    jadwal.hari = hari_buka
    jadwal.jam_buka = jam_buka_toko
    jadwal.jam_tutup = jam_tutup_toko
    jadwal.save()

    new_jadwal = {
        'pk': jadwal.pk,
        'hari': jadwal.hari, 
        'jam_buka': jadwal.jam_buka, 
        'jam_tutup': jadwal.jam_tutup,
    }
    return HttpResponse(b"CREATED", status = 201)

def delete_jadwal(request, id):
    context = {}
    jadwal = get_object_or_404(JadwalOperasi,pk = id)
    
    if(request.POST):
        jadwal.delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('/logout/'))
    response.delete_cookie('last_login')
    return response
