from django.urls import path
from detail.views import * 

app_name = "detail"

urlpatterns = [
    path('detail_toko/', detail_toko, name='detail_toko'),
    path('detail_toko/detail_json/', detail_json, name='detail_json'),
    path('jam/', jam, name='jam'),
    path('barang/', barang, name='barang'),
]