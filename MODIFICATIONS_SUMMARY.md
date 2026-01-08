# Résumé des Modifications - Intégration Frontend-Backend

## ?? Objectif

Connecter l'interface React (Frontend) avec l'API FastAPI (Backend) pour créer une application full-stack fonctionnelle.

## ? Modifications Backend

### 1. **CORS Middleware** (`Backend/main.py`)
- Ajout du middleware CORS pour permettre les requêtes cross-origin depuis le frontend
- Autorise les origines: `http://localhost:3000` et `http://localhost:3001`
- Permet toutes les méthodes HTTP et en-têtes

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## ? Nouveaux Fichiers Frontend

### 1. **Configuration API** (`Frontend/lib/api-config.ts`)
- Centralise l'URL de base de l'API
- Définit tous les endpoints disponibles
- Facilite la maintenance et les modifications d'URL

### 2. **Service API** (`Frontend/lib/api-service.ts`)
- Service complet pour tous les appels API
- Gestion automatique de l'authentification JWT
- Méthodes pour toutes les ressources:
  - Authentification (login)
  - Utilisateurs (CRUD)
  - Clients (CRUD)
  - Produits (CRUD)
  - Stocks (CRUD)
  - Commandes (CRUD)
  - Lignes de commande
  - Réservations
  - Ventes
  - Alertes stock

### 3. **Contexte d'Authentification** (`Frontend/lib/auth-context.tsx`) - MODIFIÉ
- **AVANT**: Authentification simulée (mock) basée sur l'email
- **APRÈS**: Authentification réelle via l'API
- Stockage du token JWT dans localStorage
- Décodage du token pour extraire les informations utilisateur
- Récupération des détails utilisateur depuis l'API

### 4. **Hook Panier** (`Frontend/hooks/use-cart.ts`)
- Gestion du panier d'achat côté client
- Stockage dans localStorage
- Fonctions: ajouter, supprimer, modifier quantité, vider le panier
- Calcul du total et du nombre d'articles

### 5. **Contexte Panier** (`Frontend/lib/cart-context.tsx`)
- Rend le panier accessible dans toute l'application
- Utilise le hook `use-cart` en interne

### 6. **Types TypeScript** (`Frontend/lib/types.ts`)
- Définitions TypeScript pour tous les modèles backend
- Assure la cohérence des types entre frontend et backend

### 7. **Variables d'Environnement**
- `.env.local` et `.env.local.example`
- Configure l'URL de l'API backend

## ? Fichiers Frontend Modifiés

### 1. **Page de Connexion** (`Frontend/app/login/page.tsx`)
- **AVANT**: Authentification simulée avec délai
- **APRÈS**: Appel réel à l'API `/auth/login`
- Gestion des erreurs de l'API
- Suppression des conseils sur les emails de test

### 2. **Page d'Inscription** (`Frontend/app/register/page.tsx`)
- **AVANT**: Simulation d'inscription
- **APRÈS**: Appel réel à l'API `POST /utilisateurs`
- Création d'un utilisateur avec le rôle CLIENT
- Gestion des erreurs (email déjà utilisé, etc.)

### 3. **Page Catalogue** (`Frontend/app/catalog/page.tsx`)
- **AVANT**: Produits en dur (mock data)
- **APRÈS**: Chargement dynamique depuis l'API `GET /produits`
- Affichage d'un indicateur de chargement
- Gestion des erreurs de chargement
- Filtrage par type de produit (MEDICINALE / AROMATIQUE)

### 4. **Layout Principal** (`Frontend/app/layout.tsx`)
- Ajout du `CartProvider` pour rendre le panier disponible partout
- Structure: `AuthProvider` > `CartProvider` > children

## ?? Flux d'Authentification

### Inscription
1. Utilisateur remplit le formulaire `/register`
2. Frontend ? `POST /utilisateurs` avec role="CLIENT"
3. Backend crée l'utilisateur avec mot de passe haché
4. Redirection vers `/login`

### Connexion
1. Utilisateur entre email/mot de passe sur `/login`
2. Frontend ? `POST /auth/login` (OAuth2 form)
3. Backend vérifie les identifiants
4. Backend retourne un token JWT
5. Frontend:
   - Stocke le token dans localStorage
   - Décode le token pour extraire l'ID utilisateur
   - Appelle `GET /utilisateurs/{id}` pour les détails
   - Stocke l'utilisateur dans le contexte
6. Redirection vers le dashboard approprié

### Appels API Authentifiés
- Tous les appels incluent automatiquement le header:
  ```
  Authorization: Bearer {token}
  ```
- Si le token expire ? erreur 401 ? l'utilisateur doit se reconnecter

## ?? Sécurité

### Backend
- Mots de passe hachés avec bcrypt
- Tokens JWT signés avec SECRET_KEY
- Rate limiting sur les endpoints sensibles (login, register)
- Vérification des rôles sur chaque endpoint protégé

### Frontend
- Token stocké uniquement dans localStorage (pas de cookies)
- Contexte d'authentification pour vérifier l'état de connexion
- Redirection automatique si non authentifié

## ?? Structure des Données

### Token JWT Payload
```json
{
  "sub": "123",  // ID utilisateur
  "role": "CLIENT",
  "exp": 1234567890
}
```

### User Object (Frontend)
```typescript
{
  id_utilisateur: number,
  email: string,
  nom: string,
  prenom: string,
  role: "CLIENT" | "GEST_COMMERCIAL" | "GEST_STOCK" | "ADMIN"
}
```

### Cart Item (Frontend)
```typescript
{
  id_produit: number,
  nom_produit: string,
  prix_unitaire: number,
  quantite: number,
  type_produit?: string
}
```

## ?? Prochaines Étapes

### À Implémenter

1. **Page de détail produit**
   - Charger depuis `GET /produits/{id}`
   - Afficher stock disponible
   - Bouton "Ajouter au panier"

2. **Page panier**
   - Afficher les articles du contexte panier
   - Bouton "Valider la commande"
   - Créer commande via `POST /commandes`
   - Créer lignes de commande via `POST /ligne-commandes`

3. **Dashboard Client**
   - Charger les commandes de l'utilisateur
   - Filtrer par statut
   - Afficher les détails de chaque commande

4. **Dashboard Commercial**
   - Charger toutes les commandes `GET /commandes`
   - Accepter/refuser une commande (UPDATE endpoint à créer)
   - Créer une vente via `POST /ventes`

5. **Dashboard Stock**
   - Charger les stocks `GET /stocks`
   - Charger les alertes `GET /alertes-stock`
   - Créer/modifier des stocks

6. **Dashboard Admin**
   - Vue globale
   - Gestion des utilisateurs
   - Statistiques

### Endpoints Backend À Créer

- `PUT /commandes/{id}` - Mettre à jour le statut
- `DELETE /produits/{id}` - Supprimer un produit
- `PUT /produits/{id}` - Modifier un produit
- `PUT /stocks/{id}` - Mettre à jour un stock
- `GET /commandes/user/{id}` - Commandes d'un utilisateur spécifique

## ?? Notes Importantes

1. **Base de données**: Assurez-vous que PostgreSQL est démarré et configuré
2. **Rate limiting**: Le backend limite les tentatives de connexion (5/minute)
3. **CORS**: Ajustez les origines autorisées pour la production
4. **Variables d'environnement**: Ne commitez jamais les fichiers `.env`
5. **Sécurité**: Changez la `SECRET_KEY` en production

## ?? Dépannage

### Erreur 401 sur tous les appels
- Vérifiez que le token est bien stocké dans localStorage
- Vérifiez que le header Authorization est bien envoyé
- Le token a peut-être expiré ? se reconnecter

### Erreur CORS
- Vérifiez que le middleware CORS est bien configuré dans `Backend/main.py`
- Vérifiez que l'URL du frontend est dans `allow_origins`

### Produits ne s'affichent pas
- Vérifiez que l'API backend est démarrée sur le bon port
- Vérifiez `NEXT_PUBLIC_API_URL` dans `.env.local`
- Ouvrez la console réseau du navigateur pour voir les erreurs

### Cannot read properties of undefined
- Vérifiez que le composant est bien wrappé dans les Providers
- Vérifiez l'ordre des Providers dans `layout.tsx`
