# Système d'Authentification - Mokpokpo

## Vue d'ensemble

Le système d'authentification a été implémenté avec des pages de connexion séparées pour chaque type d'utilisateur et une restriction sur l'inscription.

## Pages de Connexion

### 1. Connexion Client (`login.html`)
- **URL**: `login.html`
- **Accès**: Clients uniquement (rôle CLIENT)
- **Redirection**: `dashboard.html`
- **Fonctionnalités**:
  - Connexion avec email et mot de passe
  - Liens vers les autres pages de connexion (admin, stock, commercial)

### 2. Connexion Administrateur (`admin-login.html`)
- **URL**: `admin-login.html`
- **Accès**: Administrateurs uniquement (rôle ADMIN)
- **Redirection**: `admin.html`
- **Style**: Badge rouge pour différenciation visuelle

### 3. Connexion Gestionnaire de Stock (`stock-login.html`)
- **URL**: `stock-login.html`
- **Accès**: Gestionnaires de stock uniquement (rôle GEST_STOCK)
- **Redirection**: `stock-dashboard.html`
- **Style**: Badge violet pour différenciation visuelle

### 4. Connexion Commercial (`commercial-login.html`)
- **URL**: `commercial-login.html`
- **Accès**: Commerciaux uniquement (rôle GEST_COMMERCIAL)
- **Redirection**: `commercial-dashboard.html`
- **Style**: Badge orange pour différenciation visuelle

## Page d'Inscription (`register.html`)

### Restrictions
- **Inscription uniquement pour les CLIENTS**
- Le champ de sélection de rôle a été supprimé
- Tous les nouveaux utilisateurs sont enregistrés avec le rôle `CLIENT`
- Les gestionnaires (stock, commercial) et administrateurs doivent être créés manuellement par un admin

### Processus d'inscription
1. L'utilisateur remplit le formulaire (prénom, nom, email, mot de passe)
2. Le système envoie automatiquement le rôle `CLIENT` au backend
3. Après succès, redirection vers `login.html`

## Module d'Authentification (`js/auth.js`)

### Fonctions principales

#### `handleRoleLogin(form, expectedRole)`
Gère la connexion avec vérification du rôle:
- Envoie les identifiants au backend
- Récupère les informations utilisateur
- Vérifie que le rôle correspond à la page de connexion
- Redirige vers le tableau de bord approprié

#### `checkPageAccess(requiredRole)`
Protège les pages contre les accès non autorisés:
- Vérifie le token dans localStorage
- Vérifie le rôle de l'utilisateur
- Redirige vers la page de connexion appropriée si non authentifié
- Redirige vers le bon dashboard si mauvais rôle

#### `logout()`
Déconnecte l'utilisateur:
- Supprime le token de localStorage
- Supprime les informations utilisateur
- Redirige vers la page d'accueil

### Mapping des rôles

```javascript
const ROLE_REDIRECTS = {
    'ADMIN': 'admin.html',
    'GEST_STOCK': 'stock-dashboard.html',
    'GEST_COMMERCIAL': 'commercial-dashboard.html',
    'CLIENT': 'dashboard.html'
};
```

## Pages Protégées

Toutes les pages suivantes vérifient l'accès au chargement:

### 1. Administration (`admin.html`)
```javascript
checkPageAccess('ADMIN');
```

### 2. Gestion de Stock (`stock.html`, `stock-dashboard.html`)
```javascript
checkPageAccess('GEST_STOCK');
```

### 3. Commercial (`commercial.html`, `commercial-dashboard.html`)
```javascript
checkPageAccess('GEST_COMMERCIAL');
```

## Flux d'Authentification

### Connexion réussie
1. L'utilisateur entre ses identifiants sur sa page de connexion
2. Le système envoie une requête au backend `/auth/login`
3. Le token est stocké dans localStorage
4. Les informations utilisateur sont récupérées via `/auth/me`
5. Le système vérifie que le rôle correspond à la page de connexion
6. Redirection vers le dashboard approprié

### Accès à une page protégée
1. La page charge et exécute `checkPageAccess()`
2. Vérification du token dans localStorage
3. Vérification du rôle de l'utilisateur
4. Si non authentifié ? redirection vers page de connexion appropriée
5. Si mauvais rôle ? redirection vers le bon dashboard

### Déconnexion
1. L'utilisateur clique sur "Déconnexion"
2. La fonction `logout()` est appelée
3. Token et données utilisateur supprimés
4. Redirection vers la page d'accueil

## Sécurité

### Côté Frontend
- Vérification du rôle à chaque chargement de page
- Redirection automatique si accès non autorisé
- Token stocké dans localStorage (à améliorer avec httpOnly cookies pour la production)

### Côté Backend (à vérifier)
Le backend doit également valider:
- Les tokens JWT
- Les rôles pour chaque endpoint
- Les permissions pour chaque opération

## Création de Comptes Administrateurs et Gestionnaires

Les comptes avec les rôles ADMIN, GEST_STOCK et GEST_COMMERCIAL doivent être créés:
1. Directement en base de données
2. Via un script d'administration
3. Par un administrateur existant via le panel admin

## Points d'Amélioration Futurs

1. **Sécurité**:
   - Implémenter httpOnly cookies au lieu de localStorage
   - Ajouter un refresh token
   - Implémenter une limite de tentatives de connexion

2. **Expérience Utilisateur**:
   - Ajouter "Se souvenir de moi"
   - Implémenter la récupération de mot de passe
   - Ajouter la vérification d'email

3. **Fonctionnalités**:
   - Historique de connexion
   - Gestion des sessions actives
   - Authentification à deux facteurs (2FA)

## Fichiers Modifiés/Créés

### Nouveaux fichiers
- `Frontend/admin-login.html`
- `Frontend/stock-login.html`
- `Frontend/commercial-login.html`
- `Frontend/js/auth.js`

### Fichiers modifiés
- `Frontend/login.html` - Ajout des liens vers autres pages de connexion
- `Frontend/register.html` - Restriction au rôle CLIENT uniquement
- `Frontend/admin.html` - Ajout de la vérification d'accès
- `Frontend/stock.html` - Ajout de la vérification d'accès
- `Frontend/stock-dashboard.html` - Ajout de la vérification d'accès
- `Frontend/commercial.html` - Ajout de la vérification d'accès
- `Frontend/commercial-dashboard.html` - Ajout de la vérification d'accès

## Tests Recommandés

1. **Test d'inscription**:
   - Vérifier qu'un nouveau compte est créé avec le rôle CLIENT
   - Vérifier qu'on ne peut pas choisir d'autre rôle

2. **Test de connexion**:
   - Essayer de se connecter avec chaque type de compte
   - Vérifier les redirections appropriées
   - Tester les messages d'erreur

3. **Test de protection de pages**:
   - Essayer d'accéder aux pages admin sans être connecté
   - Essayer d'accéder aux pages admin avec un compte client
   - Vérifier les redirections automatiques

4. **Test de déconnexion**:
   - Vérifier que la déconnexion supprime les données
   - Vérifier qu'on ne peut plus accéder aux pages protégées
