# GUIDE DE TEST - Phase 3 Authentification

## ?? Demarrage

```bash
cd D:\PROJET\Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo\web-app\Mokpokpo_Project
python manage.py runserver
```

Le serveur demarre sur: http://127.0.0.1:8000/

## ? Tests a effectuer dans l'ordre

### Test 1: Page d'accueil
1. **Ouvrir le navigateur** en mode navigation privee
2. **Aller sur** http://127.0.0.1:8000/
3. **Verifier** que vous voyez:
   - Navbar verte "Ferme Mokpokpo"
   - Liens "Connexion" et "Inscription"
   - Message de bienvenue
   - Boutons "Creer un compte" et "Se connecter"

? **Resultat attendu**: Page s'affiche correctement

---

### Test 2: Inscription d'un nouveau compte
1. **Cliquer** sur "Inscription" dans la navbar
2. **Remplir le formulaire**:
   ```
   Nom: Dupont
   Prenom: Jean
   Email: jean.dupont@test.com
   Telephone: 0123456789
   Adresse: 123 Rue de Test, Paris
   Mot de passe: Test1234
   Confirmation du mot de passe: Test1234
   ```
3. **Cliquer** sur "S'inscrire"

? **Resultat attendu**:
- Message de succes: "Votre compte a ete cree avec succes !"
- Redirection vers la page d'accueil
- Navbar affiche "Mon profil" et "Deconnexion"
- Message "Bonjour Jean !"

---

### Test 3: Verifier le profil
1. **Cliquer** sur "Mon profil" dans la navbar
2. **Verifier** les informations affichees:
   - Nom complet: Jean Dupont
   - Email: jean.dupont@test.com
   - Telephone: 0123456789
   - Adresse: 123 Rue de Test, Paris
   - Role: Client
   - Date d'inscription

? **Resultat attendu**: Toutes les informations sont correctes

---

### Test 4: Deconnexion
1. **Cliquer** sur "Deconnexion" dans la navbar
2. **Verifier** le message: "Vous avez ete deconnecte."
3. **Verifier** que la navbar affiche a nouveau "Connexion" et "Inscription"

? **Resultat attendu**: Deconnexion reussie

---

### Test 5: Reconnexion
1. **Cliquer** sur "Connexion" dans la navbar
2. **Remplir le formulaire**:
   ```
   Email: jean.dupont@test.com
   Mot de passe: Test1234
   ```
3. **Cliquer** sur "Se connecter"

? **Resultat attendu**:
- Message: "Bienvenue Jean !"
- Redirection vers la page d'accueil
- Connexion reussie

---

### Test 6: Tentative de connexion avec mauvais mot de passe
1. **Se deconnecter**
2. **Aller sur** /accounts/login/
3. **Essayer de se connecter** avec:
   ```
   Email: jean.dupont@test.com
   Mot de passe: MauvaisMotDePasse
   ```

? **Resultat attendu**: Message d'erreur (pas de connexion)

---

### Test 7: Inscription avec email deja utilise
1. **Se deconnecter**
2. **Aller sur** /accounts/register/
3. **Essayer de s'inscrire** avec l'email jean.dupont@test.com

? **Resultat attendu**: Message d'erreur "Cet email est deja utilise."

---

### Test 8: Protection des pages privees
1. **Se deconnecter**
2. **Essayer d'acceder** a http://127.0.0.1:8000/accounts/profile/

? **Resultat attendu**: Redirection vers la page de connexion

---

### Test 9: Verifier dans l'admin Django
1. **Aller sur** http://127.0.0.1:8000/admin/
2. **Se connecter** avec mokpokpo_user
3. **Verifier** dans:
   - **ACCOUNTS** > **Utilisateurs**: Le nouvel utilisateur Jean Dupont est present
   - **ACCOUNTS** > **Clients**: Le profil client est cree automatiquement
   - **Authentication** > **Users**: L'utilisateur Django est cree

? **Resultat attendu**: Toutes les donnees sont presentes

---

### Test 10: Creer un utilisateur avec un role different
1. **Dans l'admin Django**, aller dans **ACCOUNTS** > **Utilisateurs**
2. **Cliquer** sur "Ajouter Utilisateur"
3. **Creer** un gestionnaire de stock:
   ```
   Nom: Martin
   Prenom: Sophie
   Email: sophie.martin@test.com
   Mot de passe: Stock1234
   Role: GEST_STOCK
   ```
4. **Enregistrer**
5. **Dans** Authentication > Users, creer un utilisateur Django:
   ```
   Username: sophie.martin@test.com
   Password: Stock1234
   ```
6. **Se deconnecter** de l'admin
7. **Se connecter** sur le site avec sophie.martin@test.com

? **Resultat attendu**: 
- Connexion reussie
- Redirection vers /dashboard/stock/
- Page "Dashboard Gestionnaire de Stock" s'affiche

---

## ?? Checklist finale

Cochez les tests reussis:

- [ ] Page d'accueil s'affiche
- [ ] Inscription fonctionne
- [ ] Profil s'affiche correctement
- [ ] Deconnexion fonctionne
- [ ] Reconnexion fonctionne
- [ ] Mauvais mot de passe refuse
- [ ] Email deja utilise detecte
- [ ] Pages privees protegees
- [ ] Admin affiche les donnees
- [ ] Redirection selon le role fonctionne

## ?? Si un test echoue

### Probleme: Erreur CSRF
**Solution**: 
1. Utiliser le mode navigation privee
2. Vider le cache du navigateur
3. Verifier CSRF_TRUSTED_ORIGINS dans settings.py

### Probleme: Page 404
**Solution**:
1. Verifier que les URLs sont bien configurees
2. Verifier l'orthographe de l'URL
3. Relancer le serveur

### Probleme: Erreur a l'inscription
**Solution**:
1. Verifier que tous les champs sont remplis
2. Verifier que les mots de passe correspondent
3. Verifier que l'email n'est pas deja utilise

### Probleme: Redirection ne fonctionne pas
**Solution**:
1. Verifier LOGIN_REDIRECT_URL dans settings.py
2. Verifier que l'utilisateur Django existe
3. Verifier le role dans le modele Utilisateur

## ?? Notes

- Toujours utiliser le **mode navigation privee** pour les tests
- Les mots de passe doivent contenir au moins 8 caracteres
- L'email sert de username pour l'authentification Django
- Chaque nouvel utilisateur inscrit a automatiquement le role CLIENT

## ? Validation finale

Si tous les tests passent, vous pouvez passer a la **Phase 4** !

La Phase 3 (Authentification) est terminee avec succes ! ??
