from django.urls import path
from .views import ProductListView, ProductListByCategoryView, CategoryListView

urlpatterns = [
    path('api/categories', CategoryListView.as_view(), name = 'categories-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/category/<str:category>/', ProductListByCategoryView.as_view(), name='product-list-by-category'),
]