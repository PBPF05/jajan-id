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
# from detail.forms import reviewform

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

def jam_json(request):
    data_barang = Barang.objects.all() 
    # (user = request.user)
    return HttpResponse(serializers.serialize("json", data_barang), content_type="application/json")

def barang_json(request):
    data_jam = JadwalOperasi.objects.all() 
    # (user = request.user)
    return HttpResponse(serializers.serialize("json", data_jam), content_type="application/json")

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