from django.urls import path
from katalog.views import  show_katalog, show_json

app_name = "katalog"

urlpatterns = [
    # TODO: Routing
    path('katalog/', show_katalog, name='katalog'), #sesuaikan dengan nama fungsi yang dibuat
    path('katalog/json/', show_json, name='json'), #sesuaikan dengan nama fungsi yang dibuat
]
