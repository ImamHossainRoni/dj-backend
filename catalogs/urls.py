from django.urls import path, include
from .views import ProductImageRetrieveAPIView, ProductImageListAPIView

urlpatterns = [
    # genders
    path('images/retrieve/<uuid:pk>/', ProductImageRetrieveAPIView.as_view(), name='retrieve_product_image'),
    path('images/all/', ProductImageListAPIView.as_view(), name='all_product_images'),

]
