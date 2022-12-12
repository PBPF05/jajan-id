from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from katalog.models import *
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @login_required(login_url="../login")
def show_katalog(request) :
    datakatalog = Toko.objects.all()
    context = {
        'datakatalog' : datakatalog
    }

    return render(request, 'katalog.html', context)

# @login_required(login_url="../login")
def show_json(request):
    datakatalog = Toko.objects.all()
    # datakatalog = Toko.objects.filter(pemilik=request.user)

    return HttpResponse(serializers.serialize('json', datakatalog))


def show_json_search(request, nama_toko):
    status = Toko.objects.filter(nama__icontains=nama_toko)
    return HttpResponse(serializers.serialize('json', status))

@csrf_exempt
def add_json_search_flutter(request, nama_toko):
    TokoUntukSearchFlutter.objects.all().delete()
    data = Toko.objects.filter(nama__icontains=nama_toko)
    for i in json.loads(serializers.serialize('json', data)):

        
        TokoUntukSearchFlutter(nama= i['fields']['nama'], kota= i['fields']['kota'], provinsi= i['fields']['provinsi'], deskripsi= i['fields']['deskripsi'], range_harga= i['fields']['range_harga'], buka= i['fields']['buka'], kondisi= i['fields']['kondisi']).save()
    return HttpResponse(serializers.serialize('json', TokoUntukSearchFlutter.objects.all()))


def show_json_search_flutter(request):
    datakatalog = TokoUntukSearchFlutter.objects.all()
    
    return HttpResponse(serializers.serialize('json', datakatalog))
