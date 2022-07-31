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
