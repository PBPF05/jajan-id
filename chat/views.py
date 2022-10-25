from typing import Any, Dict
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.defaulttags import register
from django.core.exceptions import ObjectDoesNotExist

from chat.models import Channel, Pesan
from katalog.models import Toko


@register.filter
def get_item(dictionary: Dict, key: Any) -> Any:
    return dictionary.get(key)


@register.simple_tag
def define(val=None):
    return val


def generate_sidebar(request: HttpRequest) -> dict:
    channels = Channel.objects.filter(
        Q(user=request.user.pk) | Q(toko=request.user.pk)
    ).all()

    last_messages: Dict[int, str] = {}
    for channel in channels:
        message = Pesan.objects.filter(channel=channel).order_by("-pk").first()
        if message:
            last_messages[channel.pk] = message.pesan
        else:
            last_messages[channel.pk] = "Tidak ada pesan"

    return {
        "channels": channels,
        "messages": last_messages,
    }


@login_required()
def index(request: HttpRequest):
    return render(
        request,
        "chat.html",
        {
            **generate_sidebar(request),
        },
    )


@login_required()
def chat_user(request: HttpRequest, uid: int):
    try:
        toko = Toko.objects.get(pk=request.user.pk)
        user = User.objects.get(pk=uid)
        channel, _ = Channel.objects.get_or_create(user=user, toko=toko)  # type: ignore
    except ObjectDoesNotExist:
        channel = None

    return render(
        request,
        "chat.html",
        {
            "channel": channel,
            **generate_sidebar(request),
        },
    )


@login_required()
def chat_toko(request: HttpRequest, uid: int):
    try:
        toko = Toko.objects.get(pk=uid)
        channel, _ = Channel.objects.get_or_create(user=request.user, toko=toko)  # type: ignore
    except ObjectDoesNotExist:
        channel = None

    return render(
        request,
        "chat.html",
        {
            "channel": channel,
            **generate_sidebar(request),
        },
    )
