from django.urls import path
from landing.views import show_landing, login_user, logout_user, register, login_flutter, logout_flutter, register_flutter

app_name = 'landing'

urlpatterns = [
    # TODO: Routing
    path('', show_landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login_flutter/', login_flutter, name='login_flutter'),
    path('logout_flutter/', logout_flutter, name='logout_flutter'),
    path('register_flutter/', register_flutter, name='register_flutter'),
]
