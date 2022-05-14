from django.urls import path
from .views import (
    product_detail_view, 
    all_products_view, 
    product_create_view_html,
    product_create_view_django,
    product_create_view_pure)

app_name = 'products'
urlpatterns = [
    path('<int:id>', product_detail_view, name='Product'),
    path('', all_products_view, name='Products'),
    path('createbyhtml', product_create_view_html, name='Createbyhtml'),
    path('createbydjango', product_create_view_django, name='createbydjango'),
    path('createbypureform', product_create_view_pure, name='createbypureform'),
]