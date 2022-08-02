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
    source = models.ForeignKey(ProductImageSource,
                               null=False, blank=False,
                               on_delete=models.CASCADE,
                               help_text='That refers to related product image source'
                               )
    original_url = models.URLField(max_length=200,
                                   help_text='Product image original url that can be used to get that specific image')

    original_image = models.ImageField(upload_to='images/', help_text='Actual image')
    small_image = models.ImageField(upload_to='images/small/',
                                    null=True, blank=True,
                                    help_text='Small image')
    medium_image = models.ImageField(upload_to='images/medium/',
                                     null=True, blank=True,
                                     help_text='Medium image')
    large_image = models.ImageField(upload_to='images/large/',
                                    null=True, blank=True,
                                    help_text='Large image')
    height = models.PositiveIntegerField(default=0,
                                         help_text='Actual image height')
    width = models.PositiveIntegerField(default=0, help_text='Actual image width')
    title = models.CharField(max_length=200, null=True, blank=True, help_text='Image title')
    description = models.CharField(max_length=500, null=True, blank=True,
                                   help_text='Product image description if anything needed else blank')

    class Meta:
        db_table = 'product_images'
