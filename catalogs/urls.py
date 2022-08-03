
from django.urls import path, include
from .views import ProductImageRetrieveAPIView
urlpatterns = [
    # genders
    path('all/', ProductImageRetrieveAPIView.as_view(), name='get_product_images'),

]