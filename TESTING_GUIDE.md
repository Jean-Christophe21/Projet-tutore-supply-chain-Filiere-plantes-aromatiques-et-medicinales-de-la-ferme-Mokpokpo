# Guide de Test - Intégration Frontend-Backend

Ce guide vous aide à tester l'intégration entre le frontend et le backend.

## Prérequis

1. **Backend démarré** sur `http://localhost:8000`
2. **Frontend démarré** sur `http://localhost:3000`
3. **Base de données PostgreSQL** configurée et accessible

## Tests à Effectuer

### 1. Test d'Inscription

#### Étapes:
1. Ouvrez `http://localhost:3000/register`
2. Remplissez le formulaire:
   - Prénom: Jean
   - Nom: Dupont
   - Email: jean.dupont@example.com
   - Mot de passe: test123456
   - Confirmer mot de passe: test123456
3. Cliquez sur "Créer un compte"

#### Résultat attendu:
- ? Redirection vers `/login?registered=true`
- ? L'utilisateur est créé dans la base de données
- ? Le mot de passe est haché

#### Vérification backend:
```bash
# Dans votre terminal backend, vous devriez voir:
INFO: POST /utilisateurs 200 OK
```

#### Erreurs possibles:
- ? "Cet email est déjà utilisé" ? Email déjà enregistré
- ? Erreur CORS ? Vérifiez la configuration CORS dans `Backend/main.py`

---

### 2. Test de Connexion

#### Étapes:
1. Ouvrez `http://localhost:3000/login`
2. Entrez les identifiants:
   - Email: jean.dupont@example.com
   - Mot de passe: test123456
3. Cliquez sur "Se connecter"

#### Résultat attendu:
- ? Redirection vers `/client` (dashboard client)
- ? Token JWT stocké dans localStorage
- ? Informations utilisateur stockées dans le contexte

#### Vérification dans le navigateur:
1. Ouvrez DevTools (F12)
2. Onglet "Application" > "Local Storage" > `http://localhost:3000`
3. Vous devriez voir:
   - `mokpokpo_token`: "eyJ0eXAiOiJKV1QiLCJhbGc..."
   - `mokpokpo_user`: `{"id_utilisateur":1,"email":"jean.dupont@example.com",...}`

#### Vérification backend:
```bash
INFO: POST /auth/login 200 OK
INFO: GET /utilisateurs/1 200 OK
```

#### Erreurs possibles:
- ? "Identifiants incorrects" ? Vérifiez email/mot de passe
- ? Rate limit exceeded ? Attendez 1 minute (limite: 5 tentatives/minute)

---

### 3. Test du Catalogue de Produits

#### Étapes:
1. Ouvrez `http://localhost:3000/catalog`

#### Résultat attendu:
- ? Liste des produits chargée depuis l'API
- ? Possibilité de filtrer par type (Médicinale / Aromatique)
- ? Barre de recherche fonctionnelle

#### Vérification backend:
```bash
INFO: GET /produits 200 OK
```

#### Si aucun produit n'apparaît:
Vous devez créer des produits via l'API. Deux options:

**Option 1: Via l'interface Swagger**
1. Allez sur `http://localhost:8000/docs`
2. Cliquez sur `POST /utilisateurs` et créez un admin:
   ```json
   {
     "nom": "Admin",
     "prenom": "Super",
     "email": "admin@mokpokpo.com",
     "mot_de_passe": "admin123",
     "role": "ADMIN"
   }
   ```
3. Connectez-vous avec cet admin sur le frontend
4. Utilisez l'interface pour créer des produits

**Option 2: Via curl**
```bash
# 1. Se connecter en tant qu'admin
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@mokpokpo.com&password=admin123"
# Copier le token retourné

# 2. Créer un produit
curl -X POST "http://localhost:8000/produits" \
  -H "Authorization: Bearer VOTRE_TOKEN_ICI" \
  -H "Content-Type: application/json" \
  -d '{
    "nom_produit": "Basilic",
    "type_produit": "AROMATIQUE",
    "description": "Plante aromatique fraîche",
    "usages": "Cuisine, infusions",
    "prix_unitaire": 2500
  }'
```

---

### 4. Test du Panier (Cart)

Le panier fonctionne côté client seulement pour l'instant.

#### Étapes:
1. Ouvrez la console du navigateur (F12)
2. Tapez:
   ```javascript
   // Vérifier que le panier est accessible
   localStorage.getItem('mokpokpo_cart')
   ```

#### Résultat attendu:
- ? `null` ou `[]` si le panier est vide
- ? Un tableau JSON si des articles sont présents

---

### 5. Test de Déconnexion

#### Étapes:
1. Connecté, allez sur `http://localhost:3000/logout`

#### Résultat attendu:
- ? Token et user supprimés du localStorage
- ? Redirection vers la page d'accueil
- ? Perte d'accès aux pages protégées

#### Vérification:
```javascript
// Dans la console
localStorage.getItem('mokpokpo_token') // ? null
localStorage.getItem('mokpokpo_user')  // ? null
```

---

## Tests Backend Isolés

### Test 1: Health Check
```bash
curl http://localhost:8000/
# Résultat attendu:
# {"message":"API Mokpokpo opérationnelle","docs":"/docs"}
```

### Test 2: Création d'un utilisateur
```bash
curl -X POST "http://localhost:8000/utilisateurs" \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Test",
    "prenom": "User",
    "email": "test@example.com",
    "mot_de_passe": "password123",
    "role": "CLIENT"
  }'
```

### Test 3: Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
# Copier le access_token pour les tests suivants
```

### Test 4: Get Products (authentifié)
```bash
curl -X GET "http://localhost:8000/produits" \
  -H "Authorization: Bearer VOTRE_TOKEN_ICI"
```

### Test 5: Create Product (admin uniquement)
```bash
curl -X POST "http://localhost:8000/produits" \
  -H "Authorization: Bearer ADMIN_TOKEN_ICI" \
  -H "Content-Type: application/json" \
  -d '{
    "nom_produit": "Menthe",
    "type_produit": "AROMATIQUE",
    "prix_unitaire": 1500
  }'
```

---

## Checklist Complète

### Backend
- [ ] PostgreSQL démarré
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Variables d'environnement configurées
- [ ] Serveur démarré sur port 8000
- [ ] CORS middleware configuré
- [ ] Documentation Swagger accessible sur `/docs`

### Frontend
- [ ] Dépendances installées (`pnpm install`)
- [ ] `.env.local` créé avec `NEXT_PUBLIC_API_URL`
- [ ] Serveur démarré sur port 3000
- [ ] AuthProvider dans layout
- [ ] CartProvider dans layout

### Tests Fonctionnels
- [ ] Inscription fonctionne
- [ ] Login fonctionne
- [ ] Token JWT stocké
- [ ] Catalogue charge les produits
- [ ] Filtrage par catégorie fonctionne
- [ ] Recherche fonctionne
- [ ] Déconnexion fonctionne

---

## Dépannage

### Le frontend ne se connecte pas au backend

1. **Vérifier l'URL de l'API**
   ```javascript
   // Dans la console du navigateur
   console.log(process.env.NEXT_PUBLIC_API_URL)
   // Devrait afficher: http://localhost:8000
   ```

2. **Vérifier les requêtes réseau**
   - F12 > Network > Filtrer "Fetch/XHR"
   - Vérifier que les requêtes partent vers `http://localhost:8000`

3. **Vérifier CORS**
   - Si erreur CORS ? Vérifier `Backend/main.py`
   - L'origine du frontend doit être dans `allow_origins`

### Le token ne fonctionne pas

1. **Vérifier le token**
   ```javascript
   const token = localStorage.getItem('mokpokpo_token');
   console.log(token);
   // Devrait être une longue chaîne commençant par "eyJ..."
   ```

2. **Décoder le token** (sur jwt.io)
   - Copier le token
   - Aller sur https://jwt.io
   - Vérifier le payload:
     ```json
     {
       "sub": "1",  // ID utilisateur
       "role": "CLIENT",
       "exp": 1234567890  // Date d'expiration
     }
     ```

3. **Vérifier l'expiration**
   ```javascript
   const payload = JSON.parse(atob(token.split('.')[1]));
   const isExpired = Date.now() >= payload.exp * 1000;
   console.log('Token expiré:', isExpired);
   ```

### Les produits ne s'affichent pas

1. **Vérifier qu'il y a des produits dans la DB**
   ```bash
   curl http://localhost:8000/produits
   ```

2. **Créer des produits de test**
   - Via Swagger: http://localhost:8000/docs
   - Via curl (voir exemples ci-dessus)

---

## Prochains Tests à Implémenter

1. **Test de création de commande**
   - Ajouter produits au panier
   - Valider la commande
   - Vérifier création dans DB

2. **Test de gestion des commandes (commercial)**
   - Se connecter en tant que commercial
   - Voir les commandes en attente
   - Accepter/refuser une commande

3. **Test de gestion des stocks**
   - Se connecter en tant que gestionnaire stock
   - Voir les alertes
   - Mettre à jour un stock

4. **Test des permissions**
   - Vérifier qu'un CLIENT ne peut pas accéder aux endpoints ADMIN
   - Vérifier les erreurs 403 Forbidden

---

## Contact & Support

Si vous rencontrez des problèmes:
1. Vérifiez les logs backend dans le terminal
2. Vérifiez la console du navigateur (F12)
3. Vérifiez l'onglet Network pour les erreurs HTTP
4. Consultez la documentation Swagger: http://localhost:8000/docs
