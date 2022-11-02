from django.urls import path
from chat.views import chat_toko, chat_user, get_messages, index, send_message

app_name = "chat"

urlpatterns = [
    path("messages/send", send_message),
    path("messages/<int:cid>", get_messages),
    path("user/<int:uid>", chat_user),
    path("toko/<int:uid>", chat_toko),
    path("", index),
]
