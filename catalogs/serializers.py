from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import ProductImage, ProductImageSource
from .services import get_query_to_image_width


class ProductImageSourceSerializer(ModelSerializer):
    class Meta:
        model = ProductImageSource
        exclude = [
            'created_at',
            'updated_at',
        ]


class ProductImageSerializer(ModelSerializer):
    source = ProductImageSourceSerializer()

    def to_representation(self, instance):
        """ API response modified based on some conditions"""
        request = self.context.get('request')
        query = request.query_params.get('size')

        image_width = get_query_to_image_width(query)
        original_image_url = None
        if not (not instance.original_image):
            original_image_url = request.build_absolute_uri(instance.original_image.url)

        data = {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'created_at': instance.created_at,
            'original_image_source_url': instance.original_url,
            'image_url': original_image_url,
            'previous_height': instance.height,
            'previous_width': instance.width,
            'source': ProductImageSourceSerializer(instance.source).data,
        }
        if image_width == 256:
            if not (not instance.small_image):
                data['image_url'] = request.build_absolute_uri(instance.small_image.url)
        if image_width == 1024:
            if not (not instance.medium_image):
                data['image_url'] = request.build_absolute_uri(instance.medium_image.url)
        if image_width == 2048:
            if not (not instance.large_image):
                data['image_url'] = request.build_absolute_uri(instance.large_image.url)

        return data

    class Meta:
        model = ProductImage
        exclude = [
            'updated_at',
        ]
