from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(request):
    """Vue du panier"""
    return render(request, 'sales/cart.html')


@login_required
def order_list(request):
    """Liste des commandes"""
    return render(request, 'sales/order_list.html')

