from django.urls import path
from views import show_dashboard;

app_name = "dashboard"

urlpatterns = [
    # TODO: Routing
    path('', show_dashboard, name='show_dashboard'),
    path('/json', show_data_json, name='show_json')
]
