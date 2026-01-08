# Configuration du Projet Mokpokpo - Frontend & Backend

Ce document explique comment configurer et démarrer l'application complète (Frontend + Backend).

## Architecture

- **Backend**: API FastAPI (Python) avec PostgreSQL
- **Frontend**: Application Next.js (React/TypeScript)

## Prérequis

- Python 3.8+
- Node.js 18+
- PostgreSQL
- pnpm (ou npm)

## Configuration du Backend

### 1. Installation des dépendances

```bash
cd Backend
pip install -r requirements.txt
```

### 2. Configuration de la base de données

Créez un fichier `Backend/config/.env` avec:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mokpokpo
SECRET_KEY=votre_cle_secrete_jwt
```

### 3. Démarrage du serveur

```bash
cd Backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

L'API sera accessible sur `http://localhost:8000`
Documentation interactive: `http://localhost:8000/docs`

## Configuration du Frontend

### 1. Installation des dépendances

```bash
cd Frontend
pnpm install
# ou
npm install
```

### 2. Configuration de l'environnement

Créez un fichier `Frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Démarrage de l'application

```bash
cd Frontend
pnpm dev
# ou
npm run dev
```

L'application sera accessible sur `http://localhost:3000`

## Changements Importants

### Backend

Les routeurs suivants sont disponibles:

- `/auth/login` - Connexion (POST)
- `/utilisateurs` - Gestion des utilisateurs
- `/clients` - Gestion des clients
- `/produits` - Catalogue des produits
- `/stocks` - Gestion des stocks
- `/commandes` - Gestion des commandes
- `/ligne-commandes` - Lignes de commande
- `/reservations` - Réservations
- `/ventes` - Suivi des ventes
- `/alertes-stock` - Alertes de stock

### Frontend

#### Nouveaux fichiers créés:

1. **`lib/api-config.ts`**: Configuration centralisée des endpoints API
2. **`lib/api-service.ts`**: Service pour tous les appels API
3. **`lib/auth-context.tsx`**: Contexte d'authentification mis à jour pour utiliser l'API réelle

#### Fichiers modifiés:

1. **`app/login/page.tsx`**: Utilise maintenant l'API réelle pour la connexion
2. **`app/register/page.tsx`**: Utilise l'API réelle pour l'inscription
3. **`app/catalog/page.tsx`**: Charge les produits depuis l'API

## Flux d'Authentification

1. L'utilisateur s'inscrit via `/register` ? appel à `POST /utilisateurs`
2. L'utilisateur se connecte via `/login` ? appel à `POST /auth/login`
3. Le token JWT est stocké dans `localStorage`
4. Le token est automatiquement inclus dans tous les appels API suivants

## Rôles Utilisateurs

- **CLIENT**: Peut passer des commandes et réservations
- **GEST_COMMERCIAL**: Gère les commandes et ventes
- **GEST_STOCK**: Gère les stocks et alertes
- **ADMIN**: Accès complet à toutes les fonctionnalités

## Structure du Projet

```
mokpokpo/
??? Backend/
?   ??? models/          # Modèles SQLAlchemy
?   ??? routers/         # Routes FastAPI
?   ??? schema/          # Schémas Pydantic
?   ??? security/        # Authentification & autorisation
?   ??? config/          # Configuration
?   ??? database.py      # Configuration DB
?   ??? main.py          # Point d'entrée
?
??? Frontend/
    ??? app/             # Pages Next.js
    ??? components/      # Composants React
    ??? lib/             # Services et utilitaires
    ?   ??? api-config.ts     # Configuration API
    ?   ??? api-service.ts    # Service API
    ?   ??? auth-context.tsx  # Contexte d'authentification
    ??? hooks/           # Hooks personnalisés
```

## Prochaines Étapes

Pour compléter l'intégration Frontend-Backend:

1. **Page de détail produit**: Charger les détails depuis l'API
2. **Panier d'achat**: Implémenter la création de commandes
3. **Dashboard client**: Afficher les commandes de l'utilisateur connecté
4. **Dashboard commercial**: Gérer les commandes en attente
5. **Dashboard stock**: Gérer les alertes et mouvements de stock
6. **Dashboard admin**: Vue d'ensemble du système

## Dépannage

### Erreur CORS

Si vous rencontrez des erreurs CORS, ajoutez dans `Backend/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Token expiré

Les tokens JWT expirent après un certain temps. L'utilisateur devra se reconnecter.

## Support

Pour toute question, consultez la documentation interactive de l'API sur `http://localhost:8000/docs`
