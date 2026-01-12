# ?? Guide de Test Rapide - Mokpokpo

## ? Tests Essentiels (5 minutes)

### ? Test 1 : Catalogue (Sans connexion)
1. Ouvrir `index.html` dans le navigateur
2. Cliquer sur "Catalogue" dans le menu
3. **Attendu** : Les produits doivent se charger depuis le backend
4. **Si erreur** : Vérifier la console (F12) pour voir l'erreur API

**Note** : Le backend Render peut prendre 20-30 secondes au premier chargement (cold start)

---

### ? Test 2 : Connexion CLIENT
1. Cliquer sur "Connexion" dans le menu
2. Utiliser ces identifiants de test :
   - Email : `client@test.com`
   - Mot de passe : `password123`
3. **Attendu** : 
   - Message "Connexion réussie!"
   - Redirection vers `dashboard.html`
   - Token dans localStorage (F12 ? Application ? Local Storage)

**Si l'utilisateur n'existe pas**, aller sur `register.html` et créer un compte CLIENT.

---

### ? Test 3 : Session Persistante CLIENT
1. Après connexion CLIENT réussie
2. **Fermer complètement le navigateur**
3. Rouvrir et aller sur `dashboard.html`
4. **Attendu** : Toujours connecté (pas de redirection vers login)

---

### ? Test 4 : Connexion ADMIN
1. Aller sur `admin-login.html`
2. Utiliser identifiants ADMIN :
   - Email : `admin@mokpokpo.com`
   - Mot de passe : `admin123`
3. **Attendu** :
   - Redirection vers `admin.html`
   - Token dans sessionStorage (pas localStorage)

---

### ? Test 5 : Session Temporaire ADMIN
1. Après connexion ADMIN
2. **Fermer l'onglet ou le navigateur**
3. Rouvrir et essayer d'accéder à `admin.html`
4. **Attendu** : Redirection vers `admin-login.html` (déconnexion auto)

---

### ? Test 6 : Isolation des Rôles
1. Se connecter en tant que CLIENT
2. Essayer d'accéder directement à `admin.html` via URL
3. **Attendu** : 
   - Alerte "Accès refusé"
   - Redirection vers `dashboard.html`

**Faire la même chose pour** :
- CLIENT essayant `stock-dashboard.html` ? Bloqué
- ADMIN essayant `dashboard.html` ? Bloqué
- GEST_STOCK essayant `commercial-dashboard.html` ? Bloqué

---

## ?? Dépannage Rapide

### Problème : "Impossible de contacter le serveur"
**Solutions** :
1. Vérifier que l'URL backend est correcte : `https://bd-mokpokokpo.onrender.com`
2. Attendre 30 secondes (cold start Render)
3. Ouvrir la console (F12) pour voir l'erreur exacte
4. Vérifier votre connexion Internet

### Problème : "Identifiant ou mot de passe incorrect"
**Solutions** :
1. Vérifier que le compte existe dans la base de données
2. Créer un nouveau compte via `register.html`
3. Vérifier que le backend est démarré

### Problème : Catalogue vide
**Solutions** :
1. Vérifier que `/produits` retourne des données
2. Ouvrir `https://bd-mokpokokpo.onrender.com/produits` dans le navigateur
3. Si vide, ajouter des produits via l'interface ADMIN

### Problème : Redirections infinies
**Solutions** :
1. Vider le localStorage et sessionStorage (F12 ? Application ? Clear Storage)
2. Recharger la page
3. Se reconnecter

---

## ?? Checklist Complète

| Test | Page | Statut | Notes |
|------|------|--------|-------|
| ? Chargement catalogue | products.html | | Produits visibles |
| ? Recherche produits | products.html | | Filtrage fonctionne |
| ? Connexion CLIENT | login.html | | Redirect dashboard |
| ? Session CLIENT | dashboard.html | | Persistante |
| ? Connexion ADMIN | admin-login.html | | Redirect admin |
| ? Session ADMIN | admin.html | | Temporaire |
| ? Connexion STOCK | stock-login.html | | Redirect stock |
| ? Session STOCK | stock-dashboard.html | | Temporaire |
| ? Connexion COMMERCIAL | commercial-login.html | | Redirect commercial |
| ? Session COMMERCIAL | commercial-dashboard.html | | Temporaire |
| ? Isolation CLIENT | admin.html | | Bloqué |
| ? Isolation ADMIN | dashboard.html | | Bloqué |
| ? Protection retour | admin.html | | Back button bloqué |
| ? Déconnexion | Toutes | | Redirect index |

---

## ?? Vérifications Console

### Connexion réussie - Console logs attendus :
```
Login successful, saving token
User info saved: client@test.com Role: CLIENT
```

### Chargement produits - Console logs attendus :
```
Filtered: 10 of 10 products
```

### Accès refusé - Console logs attendus :
```
Accès refusé. Cette page n'est pas accessible avec votre rôle.
```

---

## ?? Tests de Performance

### 1. Temps de Chargement
- **Page accueil** : < 2s
- **Catalogue (première fois)** : 20-30s (cold start backend)
- **Catalogue (suivantes)** : < 3s
- **Connexion** : < 2s

### 2. Recherche/Filtres
- **Recherche temps réel** : < 300ms
- **Changement catégorie** : < 100ms
- **Animation transitions** : Fluide

---

## ?? Tests Multi-Navigateurs

Tester sur :
- ? Chrome/Edge
- ? Firefox
- ? Safari (si disponible)
- ? Mobile (responsive)

---

## ?? Signaux d'Alerte

| Signal | Cause Probable | Action |
|--------|----------------|---------|
| Produits ne chargent jamais | Backend down | Vérifier Render dashboard |
| Token null | Pas connecté | Se connecter d'abord |
| 401 Unauthorized | Token expiré | Se reconnecter |
| 403 Forbidden | Mauvais rôle | Vérifier rôle utilisateur |
| CORS error | Backend config | Vérifier CORS settings |

---

## ? Critères de Validation

Le système est **opérationnel** si :
1. ? Les 4 types de connexion fonctionnent
2. ? L'isolation des rôles est effective
3. ? Les sessions temporaires se déconnectent
4. ? Le catalogue se charge
5. ? La recherche fonctionne
6. ? Pas d'erreurs console critiques

---

**Temps estimé pour tous les tests** : 15-20 minutes
**Dernière mise à jour** : 2025-01-XX
