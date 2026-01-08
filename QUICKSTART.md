# ?? Quick Start Guide - Mokpokpo

Guide de démarrage ultra-rapide pour lancer le projet en 5 minutes.

## ? Prérequis Rapides

Assurez-vous d'avoir installé:
- ? Python 3.8+ ? `python --version`
- ? Node.js 18+ ? `node --version`  
- ? PostgreSQL ? Service démarré
- ? pnpm ou npm ? `pnpm --version`

## ?? Installation en 3 Étapes

### Étape 1: Cloner et configurer la base de données

```bash
# Cloner le repo (si pas déjà fait)
git clone https://github.com/Jean-Christophe21/Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo.git
cd Projet-tutore-supply-chain-Filiere-plantes-aromatiques-et-medicinales-de-la-ferme-Mokpokpo

# Créer la base de données PostgreSQL
psql -U postgres
CREATE DATABASE mokpokpo;
\q
```

### Étape 2: Backend

```bash
cd Backend

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
# Créer Backend/config/.env avec:
# DATABASE_URL=postgresql://user:password@localhost:5432/mokpokpo
# SECRET_KEY=votre_cle_secrete_tres_longue_et_securisee

# Créer les tables et données de test
python scripts/seed_data.py

# Démarrer l'API
python -m uvicorn main:app --reload --port 8000
```

L'API est accessible sur: **http://localhost:8000**  
Documentation: **http://localhost:8000/docs**

### Étape 3: Frontend

```bash
# Ouvrir un nouveau terminal
cd Frontend

# Installer les dépendances
pnpm install
# ou: npm install

# Configurer .env.local (déjà créé)
# NEXT_PUBLIC_API_URL=http://localhost:8000

# Démarrer l'application
pnpm dev
# ou: npm run dev
```

L'application est accessible sur: **http://localhost:3000**

## ?? C'est Parti!

Ouvrez votre navigateur sur **http://localhost:3000** et connectez-vous avec:

**Compte Client**:
- Email: `pierre.dupont@example.com`
- Mot de passe: `client123`

**Compte Admin**:
- Email: `admin@mokpokpo.com`
- Mot de passe: `admin123`

## ? Méthode Alternative (Un seul script)

### Windows
```powershell
./start.ps1
```

### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

## ?? Vérifications

### Backend OK?
```bash
curl http://localhost:8000
# Devrait retourner: {"message":"API Mokpokpo opérationnelle","docs":"/docs"}
```

### Frontend OK?
Ouvrez http://localhost:3000 dans votre navigateur

### Base de données OK?
```bash
psql -U postgres -d mokpokpo -c "SELECT COUNT(*) FROM utilisateur;"
# Devrait retourner: 5
```

## ? Problèmes Courants

### Port déjà utilisé
```bash
# Backend (8000)
lsof -ti:8000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :8000   # Windows

# Frontend (3000)
lsof -ti:3000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :3000   # Windows
```

### Erreur de base de données
```bash
# Vérifier que PostgreSQL est démarré
# Windows: Services ? PostgreSQL
# Linux: sudo systemctl status postgresql
# Mac: brew services list
```

### Module Python manquant
```bash
cd Backend
pip install -r requirements.txt
```

### Dépendances Node.js manquantes
```bash
cd Frontend
rm -rf node_modules
pnpm install
```

## ?? Prochaines Étapes

1. **Tester l'inscription**: http://localhost:3000/register
2. **Explorer le catalogue**: http://localhost:3000/catalog
3. **Consulter l'API**: http://localhost:8000/docs

## ?? Besoin d'Aide?

- **Documentation complète**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)
- **Guide de test**: [TESTING_GUIDE.md](TESTING_GUIDE.md)
- **Résumé des modifications**: [MODIFICATIONS_SUMMARY.md](MODIFICATIONS_SUMMARY.MD)

## ?? Configuration Avancée

### Variables d'environnement Backend

Créer `Backend/config/.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mokpokpo
SECRET_KEY=votre_cle_secrete_jwt_minimum_32_caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Variables d'environnement Frontend

Le fichier `Frontend/.env.local` existe déjà:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## ?? Points de Contrôle

- [ ] Backend démarre sans erreur
- [ ] Frontend démarre sans erreur
- [ ] Base de données contient 5 utilisateurs
- [ ] Base de données contient 8 produits
- [ ] Connexion fonctionne
- [ ] Catalogue affiche les produits

## ?? Vous êtes prêt!

Le projet est maintenant opérationnel. Consultez [TODO.md](TODO.md) pour les prochaines fonctionnalités à implémenter.

---

**Temps estimé**: 5-10 minutes  
**Difficulté**: Facile ?????
