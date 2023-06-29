from django.urls import path
from .views import Catalog, CategoryDetail, ProductDetail

urlpatterns = [
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
