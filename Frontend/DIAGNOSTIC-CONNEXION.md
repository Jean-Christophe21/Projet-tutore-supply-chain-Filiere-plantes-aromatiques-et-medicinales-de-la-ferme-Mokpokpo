# ?? Diagnostic de Connexion - Erreur "Récupération des informations utilisateur"

## ?? Erreur Rencontrée
```
Erreur lors de la récupération des informations utilisateur
```

---

## ?? Causes Possibles

### 1. **Compte Utilisateur Inexistant**
**Symptôme** : Vous essayez de vous connecter avec `4@gmail.com`

**Solution** : Créer le compte d'abord
1. Aller sur `register.html`
2. Créer un compte avec cet email
3. Ou utiliser un compte existant

---

### 2. **Backend Non Démarré ou Inactif (Cold Start)**
**Symptôme** : Erreur de connexion au serveur

**Solution** :
1. Ouvrir : `https://bd-mokpokokpo.onrender.com/docs`
2. Attendre 20-30 secondes si la page charge
3. Réessayer la connexion

---

### 3. **Token JWT Invalide**
**Symptôme** : Login réussit mais `/auth/me` échoue

**Solution** :
```javascript
// Vérifier dans la console (F12)
1. Clic droit ? Inspecter ? Console
2. Chercher : "Login successful, saving token"
3. Si présent, chercher : "User info fetch failed: 401"
```

Si erreur 401 :
- Le token est expiré ou invalide
- Vérifier la configuration JWT du backend

---

### 4. **Problème CORS**
**Symptôme** : Erreur CORS dans la console

**Solution** :
Le backend doit avoir :
```python
# main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ??? Solutions Étape par Étape

### Solution 1 : Créer un Compte Test

1. **Ouvrir** `register.html`
2. **Remplir** :
   - Prénom : Test
   - Nom : User
   - Email : `4@gmail.com`
   - Mot de passe : `test123`
   - Type : Client
3. **Cliquer** "S'inscrire"
4. **Retourner** sur `login.html`
5. **Réessayer** la connexion

---

### Solution 2 : Utiliser un Compte Existant

Si vous avez déjà des comptes dans la base de données, utilisez-les :

**Compte Admin** :
```
Email: admin@mokpokpo.com
Mot de passe: admin123
```

**Compte Test** :
```
Email: test@example.com
Mot de passe: password123
```

---

### Solution 3 : Vérifier le Backend

#### Étape 1 : Tester l'API
Ouvrir dans le navigateur :
```
https://bd-mokpokokpo.onrender.com/
```

**Réponse attendue** :
```json
{
  "message": "API Mokpokpo opérationnelle",
  "docs": "/docs"
}
```

#### Étape 2 : Tester la Connexion Directement
1. Aller sur : `https://bd-mokpokokpo.onrender.com/docs`
2. Chercher `/auth/login`
3. Cliquer "Try it out"
4. Entrer :
   ```json
   {
     "username": "4@gmail.com",
     "password": "votre_mot_de_passe"
   }
   ```
5. Vérifier la réponse

---

### Solution 4 : Vérifier la Console du Navigateur

1. **Ouvrir** la console (F12)
2. **Chercher** les messages :

#### Messages Normaux (Connexion OK) :
```
Login successful, saving token
User info saved: 4@gmail.com Role: CLIENT
```

#### Messages d'Erreur :
```
Error fetching user info: [détails de l'erreur]
User info fetch failed: 401 {...}
```

---

## ?? Correctifs Appliqués au Code

### Amélioration 1 : Meilleure Gestion d'Erreur
```javascript
// AVANT
if (!userResponse.ok) {
    errorMessage.textContent = 'Erreur lors de la récupération...';
}

// APRÈS
if (!userResponse.ok) {
    const errorData = await userResponse.json().catch(() => ({}));
    console.error('User info fetch failed:', userResponse.status, errorData);
    errorMessage.textContent = errorData.detail || 'Erreur lors de la récupération...';
    // + Réinitialisation du bouton
}
```

### Amélioration 2 : Logs Plus Détaillés
```javascript
console.log('User info saved:', user.email, 'Role:', user.role);
console.error('User info fetch failed:', userResponse.status, errorData);
```

---

## ?? Checklist de Diagnostic

| Vérification | Comment | Résultat Attendu |
|--------------|---------|------------------|
| ? Backend actif | Ouvrir `https://bd-mokpokokpo.onrender.com/` | JSON avec "message" |
| ? Compte existe | Essayer `/docs` ? `/auth/login` | Retourne `access_token` |
| ? Token valide | Copier token ? `/auth/me` avec Bearer | Retourne infos user |
| ? Console propre | F12 ? Console | Pas d'erreurs rouges CORS |
| ? Storage OK | F12 ? Application ? Storage | Token présent |

---

## ?? Test Complet

### Scénario : Nouveau Compte

```bash
# 1. Créer le compte
POST /utilisateurs/
{
  "nom": "User",
  "prenom": "Test",
  "email": "4@gmail.com",
  "mot_de_passe": "test123",
  "role": "CLIENT"
}

# 2. Se connecter
POST /auth/login
username=4@gmail.com&password=test123

# 3. Récupérer infos
GET /auth/me
Authorization: Bearer {token}

# ? Devrait retourner :
{
  "email": "4@gmail.com",
  "nom": "User",
  "prenom": "Test",
  "role": "CLIENT",
  "id_utilisateur": 1
}
```

---

## ?? Solutions Rapides

### Problème : "4@gmail.com" n'existe pas

**Solution Immédiate** :
1. Aller sur `register.html`
2. Créer le compte avec ce mail
3. Réessayer

---

### Problème : Backend ne répond pas

**Solution Immédiate** :
1. Attendre 30 secondes (cold start Render)
2. Rafraîchir la page
3. Réessayer

---

### Problème : Erreur 401 après login

**Solution Immédiate** :
1. Vérifier que le mot de passe est correct
2. Essayer de recréer le compte
3. Vérifier les logs backend

---

## ?? Conseils

### Pour Développement
- Toujours créer un compte test en premier
- Garder la console ouverte (F12)
- Vérifier `/docs` du backend

### Pour Production
- Utiliser des emails valides
- Mots de passe forts (8+ caractères)
- Tester sur backend live

---

## ?? Support

Si le problème persiste :

1. **Vérifier** : Backend en ligne sur Render
2. **Consulter** : Logs Render du backend
3. **Tester** : `/docs` directement
4. **Vérifier** : Base de données (utilisateurs créés)

---

## ? Solution la Plus Probable

**Le compte `4@gmail.com` n'existe pas encore dans la base de données.**

### Action :
1. Créer le compte via `register.html`
2. Ou utiliser un compte existant

---

**Mise à jour** : 2025-01-XX
**Statut** : Correctifs appliqués ?
