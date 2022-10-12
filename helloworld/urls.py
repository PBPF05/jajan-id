from django.urls import path
from helloworld.views import index

app_name = 'helloworld'

urlpatterns = [
    path('', index, name='index'),
]