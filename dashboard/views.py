from django.shortcuts import render
from katalog.models import Toko
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def show_dashboard(request):
    data_toko = Toko.objects.filter(pemilik = request.user)
    return render(request, 'dashboard.html')

def show_data_json(request):
    data_toko = Toko.objects.filter(pemilik = request.user)
    return HttpResponse(serializers.serialize("json", data_toko))