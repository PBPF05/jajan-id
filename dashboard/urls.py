from django.urls import path
from dashboard.views import create_jadwal, create_toko, delete_barang, show_barang_json_byid, show_dashboard, show_data_json, show_barang_json, buka_tutup_toko, quick_add_Barang, show_jadwal_json, show_jadwal_json_byid, update_barang, update_jadwal, update_toko, delete_jadwal;

app_name = 'dashboard'

urlpatterns = [
    # TODO: Routing
    path('', show_dashboard, name='show_dashboard'),
    path('json/', show_data_json, name='show_json'),
    path('barang/json/', show_barang_json, name='show_barang_json'),
    path('jadwal/json/', show_jadwal_json, name='show_jadwal_json'),
    path('jadwal/json/<id>', show_jadwal_json_byid, name='show_jadwal_json_byid'),
    path('bukatutup/', buka_tutup_toko, name='state_toko'),
    path('tambah/', quick_add_Barang, name='tambah_barang'),
    path('delete/<id>', delete_barang, name='delete_barang'),
    path('buat-toko/', create_toko, name='create_toko'),
    path('update-toko/', update_toko, name='update_toko'),
    path('barang/json/<id>', show_barang_json_byid, name='show_barang_json_byid'),
    path('update-barang/<id>', update_barang, name='update_barang'),
    path('tambah-jadwal/', create_jadwal, name='tambah_jadwal'),
    path('update-jadwal/<id>', update_jadwal, name='update_jadwal'),
    path('delete-jadwal/<id>', delete_jadwal, name='update_jadwal')
]
