from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, BrandListView, BrandDetailView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('3col/', ProductListView.as_view(template_name='product_list_3col.html'), name='product_list_3col'),
    path('2col/', ProductListView.as_view(template_name='product_list_2col.html'), name='product_list_2col'),
    path('1col/', ProductListView.as_view(template_name='product_list_1col.html'), name='product_list_1col'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/<slug:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]
