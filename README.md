# Projet Tutoré - Supply Chain Mokpokpo

Ce dépôt contient tous les fichiers du projet tutoré du groupe 11 (LF-GI) pour la gestion de la supply chain de la ferme Mokpokpo - filière des plantes aromatiques et médicinales au Bénin.

## 🆕 Débutant ? Commencez ici !

### ⚡ EN 2 COMMANDES
```powershell
.\install.ps1    # 1. Installe tout
.\start.ps1      # 2. Démarre le projet
```

### 📖 Guide Complet
**Tout ce dont tu as besoin** 👉 **[GUIDE-COMPLET.md](GUIDE-COMPLET.md)**

Ce guide contient :
- ✅ Démarrage rapide en 3 étapes
- ✅ Toutes les commandes essentielles
- ✅ FAQ et solutions aux problèmes
- ✅ Structure du projet expliquée

## 🌱 Description

Application web full-stack permettant de gérer l'ensemble de la chaîne d'approvisionnement de la ferme Mokpokpo, de la production à la vente de plantes médicinales et aromatiques.

## 🏗️ Architecture

- **Backend**: API REST avec FastAPI (Python) - Dossier `Backend/`
- **Frontend**: Application web avec Next.js (React/TypeScript) - Dossier `Frontend/`
- **Base de données**: PostgreSQL

## 📚 Documentation

### Pour Tous 📖
- **[GUIDE-COMPLET.md](GUIDE-COMPLET.md)** - ⭐ Guide tout-en-un (Démarrage, Commandes, FAQ)

### Pour Développeurs 👨‍💻
- **[Guide d'Intégration](INTEGRATION_GUIDE.md)** - Configuration et démarrage détaillé
- **[Résumé des Modifications](MODIFICATIONS_SUMMARY.md)** - Historique des changements
- **[Guide de Test](TESTING_GUIDE.md)** - Tests et validation

## 🚀 Démarrage Rapide

### Scripts PowerShell (Windows)

Le projet inclut 2 scripts simples :

| Script | Description |
|--------|-------------|
| `.\install.ps1` | Installe tous les modules (Python + Node.js) |
| `.\start.ps1` | Démarre le Backend et le Frontend |

**Utilisation :**
```powershell
.\install.ps1    # Une seule fois
.\start.ps1      # À chaque démarrage
```

### Prérequis

- Python 3.8+
- Node.js 18+
- PostgreSQL
- pnpm (ou npm)

### 1. Configuration Backend

```bash
cd Backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

L'API sera disponible sur: http://localhost:8000  
Documentation interactive: http://localhost:8000/docs

### 2. Configuration Frontend

```bash
cd Frontend
pnpm install
pnpm dev
```

L'application sera disponible sur: http://localhost:3000

### 3. Créer des données de test

```bash
cd Backend
python scripts/seed_data.py
```

## 🔐 Comptes de Test

Après avoir exécuté le script de seed:

- **Admin**: admin@mokpokpo.com / admin123
- **Commercial**: commercial@mokpokpo.com / commercial123
- **Stock**: stock@mokpokpo.com / stock123
- **Client**: pierre.dupont@example.com / client123

## 🎯 Fonctionnalités

### Backend (API)

- ✅ Authentification JWT
- ✅ Gestion des utilisateurs (CRUD)
- ✅ Gestion des clients
- ✅ Catalogue de produits
- ✅ Gestion des stocks
- ✅ Commandes et réservations
- ✅ Suivi des ventes
- ✅ Alertes de stock
- ✅ Contrôle d'accès basé sur les rôles

### Frontend

- ✅ Inscription et connexion
- ✅ Catalogue de produits avec filtrage
- ✅ Panier d'achat (localStorage)
- 🚧 Dashboard client
- 🚧 Dashboard commercial
- 🚧 Dashboard gestionnaire de stock
- 🚧 Dashboard administrateur

## 🔧 Technologies Utilisées

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT (PyJWT)
- Bcrypt
- PostgreSQL

### Frontend
- Next.js 14
- React
- TypeScript
- Tailwind CSS
- Shadcn/ui

## 📝 Structure du Projet

```
Projet-tutore-supply-chain-Mokpokpo/
├── Backend/              # API FastAPI
│   ├── models/          # Modèles SQLAlchemy
│   ├── routers/         # Routes API
│   ├── schema/          # Schémas Pydantic
│   ├── security/        # Auth & sécurité
│   ├── scripts/         # Scripts utilitaires
│   └── main.py          # Point d'entrée
│
├── Frontend/            # Application Next.js
│   ├── app/             # Pages Next.js
│   ├── components/      # Composants React
│   ├── lib/             # Services & contextes
│   └── hooks/           # Hooks personnalisés
│
├── autres/              # Documentation et ressources
│
└── Documentation/
    ├── INTEGRATION_GUIDE.md
    ├── MODIFICATIONS_SUMMARY.md
    └── TESTING_GUIDE.md
```

## 🤝 Contributeurs

Projet réalisé par le groupe 11 - LF-GI dans le cadre d'un projet tutoré pour la ferme Mokpokpo.

## 📄 Licence

Ce projet est sous licence MIT.
