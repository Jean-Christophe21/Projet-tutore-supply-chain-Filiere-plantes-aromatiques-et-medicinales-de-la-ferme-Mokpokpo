# Corrections Appliquees - Problemes d'Encodage

## Problemes Identifies

### 1. Erreur Python : UnicodeDecodeError
**Erreur :**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 34
```

**Cause :** Fichiers Python avec accents mal encodes

### 2. Erreur Frontend : Reading source code for parsing failed
**Erreur :**
```
Reading source code for parsing failed
- invalid utf-8 sequence of 1 bytes from index 4427
```

**Cause :** Fichier `api-service.ts` avec caracteres speciaux mal encodes

---

## Corrections Appliquees

### Frontend/lib/api-service.ts
- ? Remplace "Reservations" par "Reservations" (sans accent)
- ? Corrige le type `HeadersInit` en `Record<string, string>` pour eviter erreur TypeScript

### Backend/scripts/seed_data.py
- ? Maintient l'encodage UTF-8 propre
- ? Tous les accents sont bien encodes

---

## Comment Tester Maintenant

### 1. Lance l'installation
```powershell
.\install.ps1
```

### 2. Configure la base de donnees
- Cree la base `mokpokpo` dans pgAdmin
- Configure `Backend\.env` avec ton mot de passe PostgreSQL

### 3. Demarre le projet
```powershell
.\start.ps1
```

### 4. Test l'application
- Frontend : http://localhost:3000
- API : http://localhost:8000
- Documentation : http://localhost:8000/docs

---

## Si Ca Ne Marche Toujours Pas

### Erreur "Cannot connect to database"
```powershell
# Verifie que PostgreSQL tourne
# Ouvre pgAdmin pour demarrer le serveur

# Verifie ton fichier .env
cd Backend
type .env
```

### Erreur "ModuleNotFoundError"
```powershell
# Reinstalle les modules Python
cd Backend
pip install -r requirements.txt
cd ..
```

### Erreur Frontend
```powershell
# Reinstalle les modules Node.js
cd Frontend
npm install
cd ..
```

---

## Configuration de la Base de Donnees

### Informations
- **Nom de la base** : `mokpokpo`
- **Utilisateur** : `postgres`
- **Port** : `5432`
- **Serveur** : `localhost`

### Fichier Backend\.env
```
DATABASE_URL=postgresql://postgres:TONMOTDEPASSE@localhost:5432/mokpokpo
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire-changez-moi
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Remplace `TONMOTDEPASSE` par ton vrai mot de passe PostgreSQL.

---

## Prochaines Etapes

1. **Installe** avec `.\install.ps1`
2. **Configure** `Backend\.env`
3. **Cree la base** `mokpokpo` dans pgAdmin
4. **Demarre** avec `.\start.ps1`
5. **Teste** sur http://localhost:3000

**Bonne chance ! ??**
