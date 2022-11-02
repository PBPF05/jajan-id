from django.urls import path
from landing.views import show_landing, login_user, logout_user, register

app_name = 'landing'

urlpatterns = [
    # TODO: Routing
    path('', show_landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]
