from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import ProductImageSerializer, ProductImageSourceSerializer, ProductImageListSerializer
from .models import ProductImage, ProductImageSource
from systems.paginations import StandardResultsSetPagination
from .services import is_expected_image_exist, make_expected_image


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


class ProductImageRetrieveBySourceAPIView(RetrieveAPIView):
    serializer_class = ProductImageListSerializer
    queryset = ProductImage.active_objects.all()
    lookup_field = 'source_url'

    def get(self, request, *args, **kwargs):
        source_url = kwargs.get('source_url', None)
        query = self.request.query_params.get('size')
        self.queryset = self.queryset.filter(source__name__iexact=source_url)
        if query:
            for image_obj in self.queryset:
                if not is_expected_image_exist(query, image_obj):
                    make_expected_image(query, image_obj)

        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductImageListAPIView(ListAPIView):
    serializer_class = ProductImageListSerializer
    queryset = ProductImage.active_objects.all()

    def get(self, request, *args, **kwargs):
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)
