# Guide Complet - Projet Mokpokpo

> Guide tout-en-un pour installer et utiliser le projet Mokpokpo

---

## Demarrage Rapide (2 commandes)

### Etape 1 : Installer

```powershell
.\install.ps1
```

Ce script va :
- Verifier que Python et Node.js sont installes
- Installer tous les modules Python (Backend)
- Installer tous les modules Node.js (Frontend)
- Verifier que sqlalchemy fonctionne

**Attends 3-5 minutes** que tout s'installe.

---

### Etape 2 : Configurer la base de donnees

#### A. Creer la base de donnees
1. Ouvre **pgAdmin**
2. Clic droit sur "Databases" > "Create" > "Database"
3. Nom : `mokpokpo`
4. Clique sur "Save"

#### B. Configurer la connexion
1. Va dans le dossier `Backend`
2. Copie `.env.example` et renomme-le `.env`
3. Ouvre `.env` avec Notepad
4. Change cette ligne :
   ```
   DATABASE_URL=postgresql://postgres:TONMOTDEPASSE@localhost:5432/mokpokpo
   ```
   Remplace `TONMOTDEPASSE` par ton mot de passe PostgreSQL

#### C. Creer des donnees de test (optionnel)
```powershell
cd Backend
python scripts/seed_data.py
cd ..
```

---

### Etape 3 : Demarrer le projet

```powershell
.\start.ps1
```

**Deux fenetres s'ouvrent** > Ouvre ton navigateur : **http://localhost:3000**

**Connecte-toi avec :**
- Email : `admin@mokpokpo.com`
- Mot de passe : `admin123`

C'est tout !

---

## Commandes Rapides

### Scripts PowerShell

```powershell
# Installer tous les modules (premiere fois)
.\install.ps1

# Demarrer le projet
.\start.ps1
```

### URLs Importantes

| Service | URL |
|---------|-----|
| Site web (Frontend) | http://localhost:3000 |
| API Backend | http://localhost:8000 |
| Documentation API | http://localhost:8000/docs |

### Comptes de Test

| Role | Email | Mot de passe |
|------|-------|--------------|
| Admin | admin@mokpokpo.com | admin123 |
| Commercial | commercial@mokpokpo.com | commercial123 |
| Stock | stock@mokpokpo.com | stock123 |
| Client | pierre.dupont@example.com | client123 |

---

## Questions Frequentes (FAQ)

### Erreur : "ModuleNotFoundError: No module named 'sqlalchemy'"

**Solution :**
```powershell
.\install.ps1
```

Si ca ne marche toujours pas :
```powershell
cd Backend
pip install -r requirements.txt
cd ..
```

---

### ?? Erreur : "Cannot connect to database"

**Causes possibles :**
1. PostgreSQL n'est pas démarré
2. Le fichier `.env` n'existe pas
3. Le mot de passe dans `.env` est incorrect
4. La base de données `mokpokpo` n'existe pas

**Solution :**
1. Ouvre **pgAdmin** et vérifie que PostgreSQL tourne
2. Vérifie que `Backend\.env` existe (copie `.env.example` si besoin)
3. Vérifie le mot de passe dans `.env`
4. Crée la base `mokpokpo` dans pgAdmin si elle n'existe pas

---

### ?? Erreur : "Port 8000 already in use"

**Solution :**
```powershell
# Trouve le processus qui utilise le port
netstat -ano | findstr :8000

# Tue le processus (remplace <PID> par le numéro trouvé)
taskkill /PID <PID> /F
```

Ou simplement : ferme toutes les fenêtres PowerShell et relance `.\start.ps1`

---

### ?? Le site ne se charge pas

**Vérifications :**
1. ? Les deux fenêtres PowerShell sont ouvertes (Backend + Frontend)
2. ? Pas d'erreurs dans les fenêtres PowerShell
3. ? http://localhost:8000/docs fonctionne (teste l'API)
4. ? Vide le cache du navigateur (Ctrl+Maj+Suppr)

---

### ? C'est quoi la différence entre Backend et Frontend ?

| | Frontend | Backend |
|---|----------|---------|
| **C'est quoi ?** | L'interface visible | Le serveur invisible |
| **Technologies** | Next.js, React | FastAPI, Python |
| **Rôle** | Afficher les données | Gérer les données |
| **Port** | 3000 | 8000 |

**Analogie :** Le Frontend c'est la façade d'un magasin ??, le Backend c'est l'arrière-boutique ??

---

### ? Le Frontend est-il connecté au Backend ?

**OUI !** Directement connecté via `Frontend/lib/api-service.ts`

**Flux de données :**
```
Frontend (localhost:3000)
    ? Requête HTTP
Backend API (localhost:8000)
    ? Requête SQL
Base de Données (PostgreSQL)
    ? Données
Backend API
    ? Réponse JSON
Frontend (affichage)
```

---

### ? Comment tester l'API ?

**Méthode 1 : Via la documentation interactive**
1. Va sur http://localhost:8000/docs
2. Choisis une route (ex: GET /api/produits)
3. Clique sur "Try it out"
4. Clique sur "Execute"

**Méthode 2 : Via le navigateur**
1. Ouvre le site (localhost:3000)
2. Appuie sur F12 ? onglet "Network"
3. Actualise la page
4. Tu vois toutes les requêtes envoyées au Backend

---

### ? Comment arrêter le projet ?

Ferme simplement les deux fenêtres PowerShell (Backend + Frontend)

Ou appuie sur `Ctrl+C` dans chaque fenêtre.

---

### ? C'est quoi PostgreSQL ?

Une **base de données** où sont stockées toutes les informations :
- Utilisateurs
- Produits
- Commandes
- Stocks
- etc.

**Analogie :** Un classeur géant ??? bien organisé pour ranger les données.

---

### ? C'est quoi un fichier `.env` ?

Un fichier de **configuration** avec des informations sensibles (mots de passe).

**Exemple :**
```
DATABASE_URL=postgresql://postgres:monmotdepasse@localhost:5432/mokpokpo
SECRET_KEY=ma-cle-secrete-123
```

?? **Important :** Ne partage JAMAIS ce fichier sur GitHub !

---

### ? Où trouver de l'aide ?

**Documentation officielle :**
- FastAPI : https://fastapi.tiangolo.com/
- Next.js : https://nextjs.org/docs
- PostgreSQL : https://www.postgresql.org/docs/

**Communautés :**
- Stack Overflow : https://stackoverflow.com/
- Reddit : r/learnprogramming

---

## ??? Résolution de Problèmes

### Diagnostic Automatique

Lance ce script pour vérifier que tout est OK :
```powershell
.\check-environment.ps1
```

Il vérifie :
- ? Python installé
- ? Node.js installé
- ? PostgreSQL installé
- ? Modules Backend installés
- ? Modules Frontend installés
- ? Fichier `.env` configuré

---

### Installation Manuelle

**Si les scripts automatiques ne marchent pas :**

#### Backend (Python)
```powershell
cd Backend
pip install -r requirements.txt
cd ..
```

#### Frontend (Node.js)
```powershell
cd Frontend
npm install
cd ..
```

#### Démarrage manuel
```powershell
# Terminal 1 : Backend
cd Backend
python -m uvicorn main:app --reload --port 8000

# Terminal 2 : Frontend (dans une autre fenêtre)
cd Frontend
npm run dev
```

---

### Modules Python à Installer

Si un module spécifique manque, installe-le :
```powershell
pip install sqlalchemy      # Base de données ORM
pip install fastapi          # Framework web
pip install uvicorn          # Serveur ASGI
pip install psycopg2-binary  # Connecteur PostgreSQL
pip install pydantic         # Validation des données
pip install python-jose      # JWT tokens
pip install passlib          # Hachage des mots de passe
pip install bcrypt           # Algorithme de hachage
pip install python-dotenv    # Lecture du .env
pip install python-multipart # Upload de fichiers
```

---

## ?? Structure du Projet

```
Projet-Mokpokpo/
?
??? Backend/                 # API (Python/FastAPI)
?   ??? main.py             # Point d'entrée de l'API
?   ??? database.py         # Connexion à la base de données
?   ??? requirements.txt    # Modules Python à installer
?   ??? .env                # Configuration (À CRÉER !)
?   ?
?   ??? models/             # Modèles de données (tables)
?   ??? routers/            # Routes de l'API
?   ??? schema/             # Validation des données
?   ??? security/           # Authentification JWT
?   ??? scripts/
?       ??? seed_data.py    # Données de test
?
??? Frontend/                # Interface Web (Next.js/React)
?   ??? app/                # Pages du site
?   ??? components/         # Composants réutilisables
?   ??? lib/
?   ?   ??? api-config.ts   # Configuration de l'API
?   ?   ??? api-service.ts  # Service pour communiquer avec l'API
?   ??? package.json        # Modules Node.js
?
??? fix-dependencies.ps1     # Répare les modules Python
??? install-dependencies.ps1 # Installe tout
??? check-environment.ps1    # Diagnostic
??? start.ps1               # Démarre le projet
```

---

## ?? Pour Aller Plus Loin

### Technologies Utilisées

**Backend :**
- **FastAPI** - Framework web moderne et rapide
- **SQLAlchemy** - ORM pour gérer la base de données
- **PostgreSQL** - Base de données relationnelle
- **JWT** - Authentification sécurisée
- **Bcrypt** - Hachage des mots de passe

**Frontend :**
- **Next.js** - Framework React avec routing
- **React** - Bibliothèque UI
- **TypeScript** - JavaScript avec typage
- **Tailwind CSS** - Framework CSS
- **Shadcn/ui** - Composants UI

---

### Fonctionnalités du Projet

**Backend (API) :**
- ? Authentification JWT
- ? Gestion des utilisateurs (CRUD)
- ? Gestion des clients
- ? Catalogue de produits
- ? Gestion des stocks
- ? Commandes et réservations
- ? Suivi des ventes
- ? Alertes de stock
- ? Contrôle d'accès par rôles

**Frontend :**
- ? Inscription et connexion
- ? Catalogue de produits avec filtrage
- ? Panier d'achat (localStorage)
- ?? Dashboards par rôle (en cours)

---

### Prochaines Étapes d'Apprentissage

**Niveau Débutant :**
1. Explore le code du Frontend (`Frontend/app`)
2. Regarde comment sont faites les pages
3. Modifie des textes ou couleurs
4. Teste toutes les fonctionnalités du site

**Niveau Intermédiaire :**
1. Comprends `api-service.ts` (pont Frontend/Backend)
2. Explore les routes du Backend (`Backend/routers`)
3. Regarde les modèles de données (`Backend/models`)
4. Crée un nouveau compte utilisateur

**Niveau Avancé :**
1. Ajoute une nouvelle route API
2. Crée une nouvelle page Frontend
3. Modifie la base de données
4. Ajoute de nouvelles fonctionnalités

---

## ? Checklist Complète

### Installation
- [ ] Python 3.8+ installé
- [ ] Node.js 18+ installé
- [ ] PostgreSQL installé
- [ ] `fix-dependencies.ps1` exécuté avec succès
- [ ] Base de données `mokpokpo` créée dans pgAdmin
- [ ] Fichier `Backend\.env` créé et configuré
- [ ] Données de test créées (optionnel)

### Démarrage
- [ ] `start.ps1` démarre sans erreur
- [ ] Deux fenêtres PowerShell ouvertes (Backend + Frontend)
- [ ] http://localhost:3000 affiche le site
- [ ] http://localhost:8000/docs affiche la doc API
- [ ] Je peux me connecter avec un compte test
- [ ] Je peux naviguer sur le site

### Compréhension
- [ ] Je comprends la différence Backend/Frontend
- [ ] Je sais comment ils communiquent
- [ ] Je connais les commandes de base
- [ ] Je sais où chercher de l'aide

---

## ?? Résumé Ultra-Rapide

**3 commandes pour démarrer :**

```powershell
.\fix-dependencies.ps1    # Installe les modules
# Configure Backend\.env   # (copie .env.example)
.\start.ps1              # Démarre tout
```

**3 URLs à retenir :**
- Site : http://localhost:3000
- API : http://localhost:8000
- Doc : http://localhost:8000/docs

**3 fichiers importants :**
- `Backend\.env` - Configuration
- `api-service.ts` - Pont Frontend/Backend
- `requirements.txt` - Modules Python

---

## ?? Astuces Finales

1. **Garde ce guide ouvert** pour référence rapide
2. **Lance `check-environment.ps1`** en cas de doute
3. **Consulte http://localhost:8000/docs** pour tester l'API
4. **Appuie sur F12** dans le navigateur pour voir les requêtes
5. **N'aie pas peur d'expérimenter !**

---

**?? Bravo ! Tu es prêt à utiliser Mokpokpo ! ??**

---

*Pour plus d'informations, consulte le README.md principal du projet.*
