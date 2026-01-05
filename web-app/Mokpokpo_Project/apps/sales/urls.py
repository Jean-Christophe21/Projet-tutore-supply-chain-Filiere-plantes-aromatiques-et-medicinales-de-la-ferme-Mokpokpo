from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    # Panier
    path('cart/', views.cart_view, name='cart_view'),
    
    # Commandes
    path('orders/', views.order_list, name='order_list'),
]
