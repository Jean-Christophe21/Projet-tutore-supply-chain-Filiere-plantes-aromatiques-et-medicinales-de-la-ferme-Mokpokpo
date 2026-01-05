"""
Definition of urls for Mokpokpo_Project.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from app import views


urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),
    
    # Page d'accueil
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Applications
    path('accounts/', include('apps.accounts.urls')),        # Authentification
    path('products/', include('apps.products.urls')),        # Produits
    path('stock/', include('apps.stock.urls')),              # Stock
    path('sales/', include('apps.sales.urls')),              # Ventes/Commandes
    path('dashboard/', include('apps.dashboard.urls')),      # Dashboards
    
    # Pages de l'application de base (contact, about)
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
