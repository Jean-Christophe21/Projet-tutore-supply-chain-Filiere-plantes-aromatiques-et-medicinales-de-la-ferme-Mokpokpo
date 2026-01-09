# Guide de Déploiement Complet - Mokpokpo

Ce guide détaille les étapes pour héberger l'application complète : le Backend (API + Base de données) et le Frontend (Application Next.js).

---

## ??? Partie 1 : Backend & Base de Données (Render)
*État actuel : Déjà déployé sur https://bd-mokpokokpo.onrender.com*

Cette section sert de référence pour la maintenance ou le redéploiement.

### 1. Préparation des fichiers
Assurez-vous que ces fichiers sont à la racine du dossier `Backend/` :
- `requirements.txt` : Liste des dépendances Python.
- `main.py` : Point d'entrée de l'application.
- `Procfile` (Optionnel mais recommandé sur Render) : `web: uvicorn main:app --host 0.0.0.0 --port $PORT`

### 2. Création de la Base de Données (PostgreSQL)
1. Sur Render, cliquez sur **New +** -> **PostgreSQL**.
2. Nommez-la (ex: `bdd-mokpokpo`).
3. Une fois créée, copiez l'**Internal Database URL** (pour relier au backend Render).

### 3. Déploiement du Service Web (API)
1. Sur Render, cliquez sur **New +** -> **Web Service**.
2. Connectez votre dépôt GitHub.
3. Configuration :
   - **Root Directory** : `Backend`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Variables d'environnement** (Section Environment) :
   - `DATABASE_URL` : Collez l'URL de votre base de données PostgreSQL.
   - `PYTHON_VERSION` : `3.11.0` (ou votre version locale).

---

## ?? Partie 2 : Frontend (Vercel)
*Recommandation : Vercel est l'hébergeur officiel et optimal pour Next.js.*

### 1. Préparation du Code
1. Assurez-vous que vos modifications locales sont "committées" et "pushées" sur GitHub :
   ```bash
   git add .
   git commit -m "Config production frontend"
   git push origin main
   ```

### 2. Création du projet sur Vercel
1. Créez un compte sur [vercel.com](https://vercel.com).
2. Cliquez sur **Add New...** -> **Project**.
3. Importez votre dépôt GitHub `Projet-tutore-supply-chain...`.

### 3. Configuration du Build
Vercel détecte généralement Next.js automatiquement, mais vérifiez :
- **Framework Preset** : Next.js
- **Root Directory** : Cliquez sur "Edit" et sélectionnez le dossier `Frontend`. **(Très important)**.

### 4. Variables d'Environnement
Dans la section **Environment Variables**, ajoutez :

| Nom (Key) | Valeur (Value) | Description |
|-----------|----------------|-------------|
| `NEXT_PUBLIC_API_URL` | `https://bd-mokpokokpo.onrender.com` | L'URL de votre backend Render |

*Note : Ne pas mettre de slash `/` à la fin de l'URL.*

### 5. Lancer le Déploiement
1. Cliquez sur **Deploy**.
2. Attendez que la construction (Build) se termine (environ 1-2 minutes).
3. Une fois terminé, Vercel vous donnera une URL du type `https://projet-mokpokpo.vercel.app`.

---

## ?? Partie 3 : Finalisation et Tests

### 1. Mise à jour CORS du Backend
Maintenant que vous avez l'URL de votre Frontend (ex: `https://projet-mokpokpo.vercel.app`), retournez sécuriser votre Backend.

1. Allez dans le code `Backend/main.py`.
2. Modifiez la liste `allow_origins` :
   ```python
   allow_origins=[
       "http://localhost:3000",
       "https://projet-mokpokpo.vercel.app" # Ajoutez votre nouvelle URL Vercel ici
   ]
   ```
   *(Note : Nous avons mis `"*"` temporairement, ce qui fonctionne, mais il est mieux de restreindre à l'avenir).*
3. Redéployez le Backend si vous faites ce changement.

### 2. Tests finaux
1. Ouvrez l'URL de votre Frontend déployé.
2. Essayez de vous connecter.
3. Vérifiez que le tableau de bord charge les données.

---

## ??? Résolution de problèmes courants

**Le Frontend ne se connecte pas au Backend (Erreur Network)**
- Vérifiez la variable `NEXT_PUBLIC_API_URL` dans les réglages Vercel.
- Vérifiez que le Backend sur Render est bien en statut "Live".
- Vérifiez la Console du navigateur (F12) pour voir les erreurs CORS.

**Erreur 500 sur le Backend**
- Vérifiez les "Logs" sur Render.
- Vérifiez que la base de données est bien connectée (`DATABASE_URL`).
