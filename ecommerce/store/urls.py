from django.urls import path
from .views import product_list, register, login, add_to_cart

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]