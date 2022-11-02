from django.urls import path
from detail.views import * 

app_name = "detail"

urlpatterns = [
    path('', detail_toko, name='detail_toko'),
    path('jam_json/', jam_json, name='jam_json'),
    path('barang_json/', barang_json, name='barang_json'),
    path('review/', review, name='review'),
    path('add_review/<int:id>', add_review, name='add_review'),
]