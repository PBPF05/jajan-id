from django.urls import path
from dashboard.views import show_dashboard, show_data_json, show_barang_json, buka_tutup_toko;
# tambah_barang, quick_add_Barang;

app_name = 'dashboard'

urlpatterns = [
    # TODO: Routing
    path('', show_dashboard, name='show_dashboard'),
    path('json/', show_data_json, name='show_json'),
    path('barang/json/', show_barang_json, name='show_barang_json'),
    path('bukatutup/', buka_tutup_toko, name="state_toko")
    # path('tambah/', quick_add_Barang, name="tambah_barang")
]
