from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt

from chat.models import Channel, Pesan
from chat.utils import as_json
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


def render_chat(request: HttpRequest, **kwagrs):
    return render(
        request,
        "chat.html",
        {
            **kwagrs,
            **generate_sidebar(request),
        },
    )


@login_required()
def index(request: HttpRequest):
    return render_chat(request)


@login_required()
def chat_user(request: HttpRequest, uid: int):
    if request.user.pk == uid:
        messages.error(request, "Cannot message with yourself")
        return render_chat(request)

    try:
        toko = Toko.objects.get(pk=request.user.pk)  # type: ignore
        user = User.objects.get(pk=uid)
        channel, _ = Channel.objects.get_or_create(user=user, toko=toko)  # type: ignore
    except ObjectDoesNotExist:
        channel = None

    return render_chat(request, channel=channel)


@login_required()
def chat_toko(request: HttpRequest, uid: int):
    try:
        toko = Toko.objects.get(pk=uid)
        channel, _ = Channel.objects.get_or_create(user=request.user, toko=toko)  # type: ignore
    except ObjectDoesNotExist:
        channel = None

    return render_chat(request, channel=channel)


@login_required()
def get_messages(request: HttpRequest, cid: int):
    # TODO: Check permissions!!!!!!!!!!
    try:
        channel = Channel.objects.get(pk=cid)
    except ObjectDoesNotExist:
        return HttpResponse("Not found", status=404)

    before_id = request.GET.get("before")
    after_id = request.GET.get("after")

    query = channel.pesan_set.order_by("-pk")
    if before_id:
        query = query.filter(pk__lt=int(before_id))
    if after_id:
        query = query.filter(pk__gt=int(after_id))

    messages = query.all()[:50][::-1]
    return as_json(messages)


@login_required()
@csrf_exempt
def send_message(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("Not allowed", status=405)

    data = request.POST
    try:
        channel = Channel.objects.get(pk=int(data["cid"]))
    except ObjectDoesNotExist:
        return HttpResponse("Not found", status=404)

    role = "pengirim"
    if channel.toko.pk != request.user.pk:
        role = "user"

    Pesan(pesan=data["pesan"], channel=channel, pengirim=role).save()
    return HttpResponse("OK", status=200)
