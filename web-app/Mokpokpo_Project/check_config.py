#!/usr/bin/env python
"""
Script de verification de la configuration Django
Pour le projet Mokpokpo
"""

import os
import sys
import django

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mokpokpo_Project.settings')
django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from apps.accounts.models import Utilisateur, Client
from apps.products.models import Produit
from apps.stock.models import Stock, AlerteStock
from apps.sales.models import Commande, LigneCommande, Reservation, Vente

def check_configuration():
    """Verifie la configuration de base"""
    print("=" * 60)
    print("VERIFICATION DE LA CONFIGURATION DJANGO")
    print("=" * 60)
    
    # 1. Settings
    print("\n1. SETTINGS")
    print(f"   DEBUG: {settings.DEBUG}")
    print(f"   ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"   SECRET_KEY: {'*' * 10}{settings.SECRET_KEY[-10:]}")
    print(f"   DATABASE: {settings.DATABASES['default']['ENGINE']}")
    
    # 2. CSRF
    print("\n2. CONFIGURATION CSRF")
    csrf_trusted = getattr(settings, 'CSRF_TRUSTED_ORIGINS', [])
    print(f"   CSRF_TRUSTED_ORIGINS: {csrf_trusted}")
    print(f"   CSRF_COOKIE_SECURE: {getattr(settings, 'CSRF_COOKIE_SECURE', False)}")
    
    # 3. Superutilisateurs
    print("\n3. SUPERUTILISATEURS")
    superusers = User.objects.filter(is_superuser=True)
    print(f"   Nombre: {superusers.count()}")
    for user in superusers:
        print(f"   - {user.username} ({user.email})")
    
    # 4. Modeles
    print("\n4. MODELES (nombre d'objets)")
    print(f"   Utilisateurs: {Utilisateur.objects.count()}")
    print(f"   Clients: {Client.objects.count()}")
    print(f"   Produits: {Produit.objects.count()}")
    print(f"   Stocks: {Stock.objects.count()}")
    print(f"   Alertes Stock: {AlerteStock.objects.count()}")
    print(f"   Commandes: {Commande.objects.count()}")
    print(f"   Lignes Commande: {LigneCommande.objects.count()}")
    print(f"   Reservations: {Reservation.objects.count()}")
    print(f"   Ventes: {Vente.objects.count()}")
    
    # 5. Applications installees
    print("\n5. APPLICATIONS DJANGO")
    apps_mokpokpo = [app for app in settings.INSTALLED_APPS if app.startswith('apps.')]
    for app in apps_mokpokpo:
        print(f"   ? {app}")
    
    print("\n" + "=" * 60)
    print("VERIFICATION TERMINEE")
    print("=" * 60)
    print("\nPour demarrer le serveur:")
    print("  python manage.py runserver")
    print("\nAcceder a l'admin:")
    print("  http://127.0.0.1:8000/admin/")
    print("\n")

if __name__ == '__main__':
    try:
        check_configuration()
    except Exception as e:
        print(f"\nERREUR: {e}")
        print("\nAssurez-vous que:")
        print("  1. PostgreSQL est en cours d'execution")
        print("  2. Le fichier .env est correctement configure")
        print("  3. Les migrations ont ete appliquees: python manage.py migrate")
        sys.exit(1)
