# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### À venir
- Dashboard client
- Dashboard commercial
- Dashboard gestionnaire de stock
- Dashboard administrateur
- Validation de commande
- Upload d'images produits

## [1.0.0] - 2026-01-07

### Ajouté

#### Backend
- Configuration CORS pour permettre les requêtes depuis le frontend
- Script `scripts/seed_data.py` pour créer des données de test
  - 5 utilisateurs (admin, commercial, stock, 2 clients)
  - 8 produits (plantes médicinales et aromatiques)
  - Stocks pour chaque produit
  - Commande exemple

#### Frontend
- Service API complet (`lib/api-service.ts`)
  - Méthodes pour toutes les ressources (auth, users, products, orders, etc.)
  - Gestion automatique du token JWT
  - Gestion d'erreurs unifiée
- Configuration centralisée des endpoints (`lib/api-config.ts`)
- Hook personnalisé pour le panier (`hooks/use-cart.ts`)
  - Ajout, suppression, modification d'articles
  - Calcul du total
  - Persistance dans localStorage
- Contexte panier (`lib/cart-context.tsx`)
- Types TypeScript pour tous les modèles backend (`lib/types.ts`)
- Variables d'environnement (`.env.local`, `.env.local.example`)

#### Documentation
- Guide d'intégration complet (`INTEGRATION_GUIDE.md`)
- Résumé détaillé des modifications (`MODIFICATIONS_SUMMARY.md`)
- Guide de test (`TESTING_GUIDE.md`)
- TODO avec roadmap (`TODO.md`)
- Guide de contribution (`CONTRIBUTING.md`)
- Résumé complet des travaux (`WORK_SUMMARY.md`)
- Changelog (`CHANGELOG.md`)

#### Scripts
- Script de démarrage Linux/Mac (`start.sh`)
- Script de démarrage Windows (`start.ps1`)

#### Configuration
- `.gitignore` amélioré pour Python, Node.js, et environnements

### Modifié

#### Backend
- `main.py`: Ajout du middleware CORS

#### Frontend
- `app/login/page.tsx`: Utilisation de l'API réelle pour la connexion
- `app/register/page.tsx`: Utilisation de l'API réelle pour l'inscription
- `app/catalog/page.tsx`: Chargement dynamique des produits depuis l'API
- `app/layout.tsx`: Ajout du CartProvider
- `lib/auth-context.tsx`: Refonte complète pour utiliser l'API réelle
  - Authentification JWT
  - Décodage du token
  - Récupération des données utilisateur

#### Documentation
- `README.md`: Mise à jour complète avec architecture et démarrage rapide

### Sécurité

#### Backend
- Hachage bcrypt des mots de passe
- Tokens JWT signés avec SECRET_KEY
- Rate limiting sur les endpoints d'authentification (5/minute)
- Contrôle d'accès basé sur les rôles
- Validation des données avec Pydantic

#### Frontend
- Stockage sécurisé du token JWT
- Inclusion automatique du token dans les requêtes
- Validation côté client

## [0.1.0] - 2025-12-XX

### Ajouté

#### Backend
- API FastAPI avec endpoints:
  - `/auth/login` - Authentification
  - `/utilisateurs` - Gestion des utilisateurs
  - `/clients` - Gestion des clients
  - `/produits` - Catalogue de produits
  - `/stocks` - Gestion des stocks
  - `/commandes` - Gestion des commandes
  - `/ligne-commandes` - Lignes de commande
  - `/reservations` - Réservations
  - `/ventes` - Suivi des ventes
  - `/alertes-stock` - Alertes de stock
- Modèles SQLAlchemy pour toutes les entités
- Schémas Pydantic pour la validation
- Système d'authentification JWT
- Contrôle d'accès basé sur les rôles

#### Frontend
- Application Next.js 14 avec TypeScript
- Pages:
  - Page d'accueil
  - Connexion (mock)
  - Inscription (mock)
  - Catalogue (mock data)
  - À propos
  - Contact
- Composants UI (Shadcn/ui)
- Authentification simulée

#### Base de données
- Modèle relationnel PostgreSQL
- Tables: utilisateur, client, produit, stock, commande, ligne_commande, reservation, ligne_reservation, vente, alerte_stock

---

## Format

Les types de changements sont:
- **Ajouté** pour les nouvelles fonctionnalités
- **Modifié** pour les changements dans les fonctionnalités existantes
- **Déprécié** pour les fonctionnalités qui seront bientôt supprimées
- **Supprimé** pour les fonctionnalités supprimées
- **Corrigé** pour les corrections de bugs
- **Sécurité** en cas de vulnérabilités

---

[Non publié]: https://github.com/Jean-Christophe21/Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Jean-Christophe21/Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo/releases/tag/v1.0.0
[0.1.0]: https://github.com/Jean-Christophe21/Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo/releases/tag/v0.1.0
