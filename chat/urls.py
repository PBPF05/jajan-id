from django.urls import path

from chat.views import (
    chat_toko,
    chat_user,
    get_chatlist,
    get_messages,
    index,
    send_message,
    send_message_json
)

app_name = "chat"

urlpatterns = [
    path("messages/json/send", send_message_json),
    path("messages/send", send_message),
    path("messages/<int:cid>", get_messages),
    path("user/<int:uid>", chat_user),
    path("toko/<int:uid>", chat_toko),
    path("get", get_chatlist),
    path("", index),
]
