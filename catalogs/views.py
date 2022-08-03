from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import ProductImageSerializer, ProductImageSourceSerializer
from .models import ProductImage, ProductImageSource
from systems.paginations import StandardResultsSetPagination


# Create your views here.

class ProductImageRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.active_objects.all()

    def get(self, request, *args, **kwargs):
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)
