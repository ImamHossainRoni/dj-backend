from django.db import models
from systems.models import BaseModel


# Create your models here.

class ProductImageSource(BaseModel):
    """ To store product image source information"""

    source_url = models.URLField(max_length=200,
                                 help_text='Product image source url where image data will be scrapping')
    name = models.CharField(max_length=200, null=True, blank=True,
                            help_text='Image source name, like - `Unsplash`')

    class Meta:
        db_table = 'product_image_sources'


class ProductImage(BaseModel):
    """ To store image information with metadata"""
    original_url = models.URLField(max_length=200,
                                   help_text='Product image original url that can be used to get that specific image')

    original_image = models.ImageField(upload_to='images/', help_text='Actual image')
    height = models.PositiveIntegerField(default=0, help_text='Actual image height')
    width = models.PositiveIntegerField(default=0, help_text='Actual image width')
    title = models.CharField(max_length=200, null=True, blank=True, help_text='Image title')
    description = models.CharField(max_length=500, null=True, blank=True,
                                   help_text='Product image description if anything needed else blank')

    class Meta:
        db_table = 'product_images'
