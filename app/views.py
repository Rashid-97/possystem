from django.http import FileResponse, HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404

from pos.models import Product


def check_image_perm(request, pk):
    image = get_object_or_404(Product, pk=pk)
    print(pk)
    if int(pk) == 6:
        return HttpResponse(image.picture, content_type='image/jpeg')
    return HttpResponseForbidden("Access denied")
