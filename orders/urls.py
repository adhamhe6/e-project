from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.view_orders, name='view_orders'),
    path('invoice/<int:order_id>/', views.view_invoice, name='view_invoice'),
]