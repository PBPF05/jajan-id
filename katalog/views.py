from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from katalog.models import Toko
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.core import serializers
import json


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