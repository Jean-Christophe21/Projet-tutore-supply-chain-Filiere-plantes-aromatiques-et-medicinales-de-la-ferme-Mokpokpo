# Guide de Demarrage Rapide - Projet Mokpokpo

## Corrections appliquees

### 1. Fichier settings.py
- ? SECRET_KEY corrigee
- ? DEBUG configure pour le developpement
- ? ALLOWED_HOSTS configure avec localhost
- ? CSRF_TRUSTED_ORIGINS ajoute
- ? CSRF_COOKIE_SECURE et SESSION_COOKIE_SECURE configures

### 2. Base de donnees
- ? Migrations creees et appliquees
- ? Toutes les tables PostgreSQL creees
- ? Superutilisateur: mokpokpo_user

### 3. Sessions
- ? Anciennes sessions nettoyees

## Pour se connecter a l'admin Django

### Etape 1: Demarrer le serveur
```bash
cd D:\PROJET\Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo\web-app\Mokpokpo_Project
python manage.py runserver
```

### Etape 2: Ouvrir le navigateur
**IMPORTANT**: Utiliser le mode navigation privee/incognito pour eviter les problemes de cache

- Chrome/Edge: Ctrl + Shift + N
- Firefox: Ctrl + Shift + P

### Etape 3: Acceder a l'admin
URL: http://127.0.0.1:8000/admin/

**Credentials du superutilisateur:**
- Username: mokpokpo_user
- Password: [Votre mot de passe defini lors de la creation]

### Etape 4: Si vous avez oublie le mot de passe
Recreer un superutilisateur:
```bash
python manage.py createsuperuser
```

## Que faire si l'erreur CSRF persiste

### Solution 1: Nettoyer completement le cache
1. Fermer TOUS les onglets de votre navigateur
2. Vider le cache (Ctrl + Shift + Delete)
3. Redemarrer le navigateur
4. Utiliser le mode navigation privee

### Solution 2: Nettoyer les sessions Django
```bash
python manage.py clearsessions
```

### Solution 3: Verifier la configuration
```bash
python manage.py check
```

### Solution 4: Redemarrer le serveur
1. Arreter le serveur (Ctrl + C)
2. Attendre 2-3 secondes
3. Relancer: `python manage.py runserver`

## URLs disponibles

### Admin Django
http://127.0.0.1:8000/admin/
- Gerer tous les modeles
- Ajouter/Modifier/Supprimer des donnees

### Interface utilisateur
http://127.0.0.1:8000/
- Page d'accueil du site

### Autres pages
- Contact: http://127.0.0.1:8000/contact/
- About: http://127.0.0.1:8000/about/
- Login: http://127.0.0.1:8000/login/

## Modeles disponibles dans l'admin

### apps.accounts
- Utilisateur (utilisateur)
- Client (client)

### apps.products
- Produit (produit)

### apps.stock
- Stock (stock)
- AlerteStock (alerte_stock)

### apps.sales
- Commande (commande)
- LigneCommande (ligne_commande)
- Reservation (reservation)
- LigneReservation (ligne_reservation)
- Vente (vente)

## Commandes utiles

```bash
# Verifier la configuration
python manage.py check

# Voir les migrations
python manage.py showmigrations

# Creer un superutilisateur
python manage.py createsuperuser

# Lancer le shell Django
python manage.py shell

# Nettoyer les sessions
python manage.py clearsessions

# Voir les URLs configurees
python manage.py show_urls  # Necessite django-extensions
```

## Tester les modeles dans le shell

```bash
python manage.py shell
```

```python
# Importer les modeles
from apps.accounts.models import Utilisateur, Client
from apps.products.models import Produit
from apps.stock.models import Stock, AlerteStock
from apps.sales.models import Commande, Vente

# Creer un utilisateur
utilisateur = Utilisateur.objects.create(
    nom="Dupont",
    prenom="Jean",
    email="jean.dupont@example.com",
    mot_de_passe="password123",
    role="CLIENT"
)

# Creer un client
client = Client.objects.create(
    telephone="0123456789",
    adresse="123 Rue Example",
    id_utilisateur=utilisateur
)

# Creer un produit
produit = Produit.objects.create(
    nom_produit="Basilic",
    type_produit="Aromatique",
    description="Plante aromatique",
    usages="Cuisine",
    prix_unitaire=5.50
)

# Creer un stock
stock = Stock.objects.create(
    quantite_disponible=100,
    seuil_minimal=10,
    id_produit=produit
)

# Voir tous les produits
Produit.objects.all()

# Filtrer les produits
Produit.objects.filter(type_produit="Aromatique")
```

## Structure du projet

```
Mokpokpo_Project/
??? Mokpokpo_Project/          # Configuration principale
?   ??? settings.py            # ? CORRIGE
?   ??? urls.py
?   ??? wsgi.py
??? apps/                      # Applications Django
?   ??? accounts/              # ? Modeles crees
?   ??? products/              # ? Modeles crees
?   ??? stock/                 # ? Modeles crees
?   ??? sales/                 # ? Modeles crees
?   ??? dashboard/
??? app/                       # Application de base
?   ??? templates/
?   ??? static/
??? .env                       # ? Configure
??? manage.py
??? db.sqlite3 (ou PostgreSQL) # ? Migrations appliquees
```

## Fichiers de documentation crees

1. **MODELS_STRUCTURE.md** - Structure detaillee de tous les modeles
2. **CORRECTION_ERREUR_CSRF.md** - Guide de resolution de l'erreur CSRF
3. **GUIDE_DEMARRAGE.md** (ce fichier) - Guide de demarrage rapide

## Prochaines etapes

1. ? Se connecter a l'admin Django
2. ? Verifier que tous les modeles sont accessibles
3. Creer des donnees de test
4. Developper les vues et templates pour chaque application
5. Implementer l'authentification personnalisee
6. Creer les dashboards par role

## Support

Si vous rencontrez des problemes:
1. Consulter CORRECTION_ERREUR_CSRF.md
2. Verifier les logs du serveur dans le terminal
3. Utiliser le mode navigation privee du navigateur
4. Verifier le fichier .env
5. Verifier que PostgreSQL est en cours d'execution
