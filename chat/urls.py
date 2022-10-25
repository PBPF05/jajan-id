from django.urls import path
from chat.views import chat_toko, chat_user, index

app_name = "chat"

urlpatterns = [
    path("user/<int:uid>", chat_user),
    path("toko/<int:uid>", chat_toko),
    path("", index),
]
