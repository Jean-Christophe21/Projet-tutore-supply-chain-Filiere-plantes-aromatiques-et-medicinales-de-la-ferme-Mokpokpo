from django.shortcuts import render
from .models import Produit


def product_list(request):
    """Liste des produits"""
    produits = Produit.objects.all()
    context = {
        'produits': produits
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id):
    """Detail d'un produit"""
    from django.shortcuts import get_object_or_404
    produit = get_object_or_404(Produit, id_produit=product_id)
    context = {
        'produit': produit
    }
    return render(request, 'products/product_detail.html', context)

