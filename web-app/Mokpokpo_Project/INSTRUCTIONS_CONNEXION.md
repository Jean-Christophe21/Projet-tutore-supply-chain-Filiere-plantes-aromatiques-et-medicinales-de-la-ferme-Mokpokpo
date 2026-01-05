# INSTRUCTIONS DE CONNEXION - Admin Django

## ? Toutes les corrections ont ete appliquees avec succes !

## Etapes pour se connecter a l'admin

### 1?? Demarrer le serveur Django
```bash
cd D:\PROJET\Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo\web-app\Mokpokpo_Project
python manage.py runserver
```

Vous devriez voir:
```
System check identified no issues (0 silenced).
Django version X.X.X, using settings 'Mokpokpo_Project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 2?? Ouvrir le navigateur EN MODE NAVIGATION PRIVEE

**?? IMPORTANT: Utilisez toujours le mode navigation privee pour eviter les problemes de cache**

- **Chrome/Edge**: Appuyez sur `Ctrl + Shift + N`
- **Firefox**: Appuyez sur `Ctrl + Shift + P`

### 3?? Acceder a l'admin Django

Dans la barre d'adresse, tapez:
```
http://127.0.0.1:8000/admin/
```

OU
```
http://localhost:8000/admin/
```

### 4?? Se connecter

**Identifiants du superutilisateur:**
- **Username**: `mokpokpo_user`
- **Password**: [Le mot de passe que vous avez defini]

Si vous avez oublie le mot de passe, voir la section ci-dessous.

---

## ?? Si vous avez oublie le mot de passe

### Option 1: Changer le mot de passe via Django
```bash
python manage.py changepassword mokpokpo_user
```

### Option 2: Creer un nouveau superutilisateur
```bash
python manage.py createsuperuser
```
Puis suivez les instructions:
- Username: admin (ou autre)
- Email: admin@mokpokpo.com (ou autre)
- Password: [Votre mot de passe]
- Password (again): [Repetez le mot de passe]

---

## ? Si vous voyez encore l'erreur CSRF

### Solution rapide:
1. **Fermez TOUS les onglets** de votre navigateur
2. **Redemarrez le navigateur**
3. **Ouvrez en mode navigation privee**
4. **Reessayez**

### Si ca ne fonctionne pas:
```bash
# 1. Arreter le serveur (Ctrl + C)

# 2. Nettoyer les sessions
python manage.py clearsessions

# 3. Redemarrer le serveur
python manage.py runserver

# 4. Reessayer avec le navigateur en mode prive
```

---

## ?? Pages disponibles dans l'admin

Une fois connecte, vous verrez:

### AUTHENTICATION AND AUTHORIZATION
- Groups
- Users (utilisateurs Django par defaut)

### ACCOUNTS
- **Utilisateurs** - Gestion des utilisateurs Mokpokpo
- **Clients** - Gestion des clients

### PRODUCTS
- **Produits** - Gestion des plantes aromatiques et medicinales

### STOCK
- **Stocks** - Gestion des stocks de produits
- **Alertes Stock** - Gestion des alertes de stock

### SALES
- **Commandes** - Gestion des commandes
- **Lignes Commande** - Details des commandes
- **Reservations** - Gestion des reservations
- **Lignes Reservation** - Details des reservations
- **Ventes** - Enregistrement des ventes

---

## ?? Tester que tout fonctionne

### Test 1: Creer un produit
1. Aller dans **PRODUCTS** > **Produits**
2. Cliquer sur **Ajouter Produit**
3. Remplir:
   - Nom produit: `Basilic`
   - Type produit: `Aromatique`
   - Prix unitaire: `5.50`
4. Cliquer sur **Enregistrer**

### Test 2: Creer un utilisateur
1. Aller dans **ACCOUNTS** > **Utilisateurs**
2. Cliquer sur **Ajouter Utilisateur**
3. Remplir:
   - Nom: `Dupont`
   - Prenom: `Jean`
   - Email: `jean.dupont@example.com`
   - Mot de passe: `Password123`
   - Role: `CLIENT`
4. Cliquer sur **Enregistrer**

---

## ?? Documents de reference

1. **RESUME.md** - Resume de toutes les corrections
2. **CORRECTION_ERREUR_CSRF.md** - Guide detaille de l'erreur CSRF
3. **GUIDE_DEMARRAGE.md** - Guide complet de demarrage
4. **MODELS_STRUCTURE.md** - Structure des modeles Django
5. **check_config.py** - Script de verification

---

## ?? Support

Si vous rencontrez des problemes:

1. Verifier que PostgreSQL est actif
2. Verifier le fichier `.env`
3. Executer: `python check_config.py`
4. Consulter les documents de reference
5. Verifier les logs du serveur Django dans le terminal

---

## ? Checklist finale avant de commencer

- [ ] PostgreSQL est en cours d'execution
- [ ] Le serveur Django demarre sans erreur
- [ ] Le navigateur est en mode navigation privee
- [ ] L'URL est http://127.0.0.1:8000/admin/
- [ ] Vous avez les bons identifiants

**Tout est pret ! Bonne utilisation !** ??
