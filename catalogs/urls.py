from django.urls import path, include
from .views import ProductImageRetrieveAPIView, ProductImageListAPIView, ProductImageRetrieveBySourceAPIView

urlpatterns = [
    # genders
    path('images/retrieve/<uuid:pk>/', ProductImageRetrieveAPIView.as_view(), name='retrieve_product_image'),
    path('images/retrieve-by-source-url/<str:source_url>/', ProductImageRetrieveBySourceAPIView.as_view(),
         name='retrieve_product_image_by_source_url'),
    path('images/all/', ProductImageListAPIView.as_view(), name='all_product_images'),

]
