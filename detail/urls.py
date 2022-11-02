from django.urls import path
from detail.views import * 

app_name = "detail"

urlpatterns = [
    path('detail_toko/', detail_toko, name='detail_toko'),
    path('detail_toko/jam_json/', jam_json, name='jam_json'),
    path('detail_toko/barang_json/', barang_json, name='barang_json'),
    # path('detail_toko/review/', review, name='review'),
]