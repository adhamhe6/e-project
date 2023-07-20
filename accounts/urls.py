from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logine/', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
]
""" path('add_contact_number/', views.add_contact_number, name='add_contact_number'),
    path('add_delivery_address/', views.add_delivery_address, name='add_delivery_address'),
    path('add_payment_option/', views.add_payment_option, name='add_payment_option'), """