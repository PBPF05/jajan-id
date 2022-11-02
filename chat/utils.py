from typing import Iterable


from django.db.models import Model
from django.core import serializers
from django.http import HttpResponse


def as_json(query: Iterable[Model], **kwargs):
    return HttpResponse(
        serializers.serialize("json", query),
        content_type="application/json",
        **kwargs,
    )
