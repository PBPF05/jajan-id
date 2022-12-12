from django.urls import path

from katalog.views import show_json, show_json_search, show_katalog, add_json_search_flutter, show_json_search_flutter

app_name = "katalog"

urlpatterns = [
    # TODO: Routing
    path("json_searched_flutter/", show_json_search_flutter, name="show_json_search_flutter"),
    path(
        "json_flutter/<str:nama_toko>/", add_json_search_flutter, name="show_json_search_flutter"
    ),
    path("", show_katalog, name="katalog"),  # sesuaikan dengan nama fungsi yang dibuat
    path("json/", show_json, name="json"),  # sesuaikan dengan nama fungsi yang dibuat
    path("json/<str:nama_toko>/", show_json_search, name="json"),  # sesuaikan dengan nama fungsi yang dibuat
]
