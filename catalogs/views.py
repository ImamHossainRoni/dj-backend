from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import ProductImageSerializer, ProductImageSourceSerializer
from .models import ProductImage, ProductImageSource
from systems.paginations import StandardResultsSetPagination
from systems.enum import ImageSize
from PIL import Image
import os, sys
from django.conf import settings


# Create your views here.

class ProductImageRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.active_objects.all()
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        query = self.request.query_params.get('size')
        if query:
            self.queryset = self.queryset.filter(id=pk)
            for image_obj in self.queryset:
                if not is_expected_image_exist(query, image_obj):
                    make_expected_image(query, image_obj)
        return super().get(request, args, kwargs)


def is_expected_image_exist(query, image_obj):
    """ Checking expected image exist or not"""
    image_width = get_query_to_image_width(query)
    res = False
    if image_width == 256:
        res = False if not image_obj.small_image else True

    if image_width == 1024:
        res = False if not image_obj.medium_image else True

    if image_width == 2048:
        res = False if not image_obj.large_image else True

    return res


def make_expected_image(query, image_obj):
    """ Make expected image if not exist"""
    original_height = image_obj.height
    original_width = image_obj.width
    height, width = get_expected_image_size(query, original_height, original_width)
    if width:
        original_image = Image.open(image_obj.original_image.path)
        new_image = original_image.resize((width, height), Image.ANTIALIAS)
        path = os.path.join(settings.BASE_DIR, 'media/')
        f, e = os.path.splitext(path)
        image_name = query.lower() + str(image_obj.id) + '.png'
        new_image.save(f + image_name, 'PNG', quality=90)
        img = Image.open(f + image_name)

        if width == 256:
            image_obj.small_image = image_name
        if width == 1024:
            image_obj.medium_image = image_name
        if width == 2048:
            image_obj.large_image = image_name

        image_obj.save()
    return True


def get_query_to_image_width(query):
    """Get given width from query params"""
    query = query.upper()
    image_width = 0
    if ImageSize.has_key(query):
        image_width = ImageSize[query].value
    return image_width


def get_expected_image_size(query, original_height, original_width):
    """ Get expected image size ratio from query params"""
    image_width = get_query_to_image_width(query)
    expected_height = int((image_width * original_height) / original_width)
    return expected_height, image_width


class ProductImageListAPIView(ListAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.active_objects.all()

    def get(self, request, *args, **kwargs):
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)
