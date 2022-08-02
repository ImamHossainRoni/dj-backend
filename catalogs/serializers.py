from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import ProductImage, ProductImageSource


class ProductImageSourceSerializer(ModelSerializer):
    class Meta:
        model = ProductImageSource
        exclude = [
            'created_at',
            'updated_at',
        ]


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = [
            'created_at',
            'updated_at',
        ]
