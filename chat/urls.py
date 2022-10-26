from django.urls import path
from chat.views import chat_toko, chat_user, get_messages, index

app_name = "chat"

urlpatterns = [
    path("messages/<int:cid>", get_messages),
    path("user/<int:uid>", chat_user),
    path("toko/<int:uid>", chat_toko),
    path("", index),
]
