from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from detail.models import JadwalOperasi
from detail.models import Barang, ReviewBarang
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
from detail.forms import reviewform

# @login_required(login_url="../login")
def detail_toko(request):
    data_jam = JadwalOperasi.objects.all()
    data_barang = Barang.objects.all()
    context = {
        'detail.jadwaloperasi' : data_jam,
        'detail.barang' : data_barang,
    }
    return render(request, 'detail.html', context)

def jam_json(request):
    data_barang = Barang.objects.all() 
    return HttpResponse(serializers.serialize("json", data_barang), content_type="application/json")

def barang_json(request):
    data_jam = JadwalOperasi.objects.all() 
    return HttpResponse(serializers.serialize("json", data_jam), content_type="application/json")

# @login_required(login_url='.../login/')
def review(request):
    if request.method == "POST":
        form = reviewform(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("dashboard:"))
            return response
    else:
        form = reviewform()
    return render(request, "review.html")

@csrf_exempt
def add_review(request, id):
    if request.method == 'POST':
        review = request.POST.get('review')
        objreview = ReviewBarang.objects.create(
            barang = Barang.objects.filter(pk=id), comment = review
        )
        return JsonResponse(
            {
                "fields": {
                    "review": objreview.comment,
                },
            },
        )
    return HttpResponseBadRequest()
