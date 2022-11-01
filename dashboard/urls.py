from django.urls import path
from dashboard.views import create_toko, delete_barang, show_barang_json_byid, show_dashboard, show_data_json, show_barang_json, buka_tutup_toko, quick_add_Barang, update_toko;

app_name = 'dashboard'

urlpatterns = [
    # TODO: Routing
    path('', show_dashboard, name='show_dashboard'),
    path('json/', show_data_json, name='show_json'),
    path('barang/json/', show_barang_json, name='show_barang_json'),
    path('bukatutup/', buka_tutup_toko, name='state_toko'),
    path('tambah/', quick_add_Barang, name='tambah_barang'),
    path('delete/<id>', delete_barang, name='delete_barang'),
    path('buat-toko/', create_toko, name='create_toko'),
    path('update-toko/', update_toko, name='update_toko'),
    path('barang/json/<id>', show_barang_json_byid, name='show_barang_json_byid')
]
