from django.core.exceptions import ObjectDoesNotExist

from katalog.models import Toko


def inject_toko(get_response):
    def middleware(request):
        if request.user:
            try:
                toko = Toko.objects.get(pk=request.user.pk)
            except ObjectDoesNotExist:
                toko = None

            request.user.toko = toko
            request.user.is_seller = toko is not None

        response = get_response(request)
        return response

    return middleware
