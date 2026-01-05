# Resolution de l'erreur CSRF - Django Admin

## Probleme
```
Forbidden (403)
CSRF verification failed. Request aborted.
Reason given for failure: CSRF token from POST incorrect.
```

## Causes identifiees

1. **SECRET_KEY mal configuree** - Etait en dur au lieu d'utiliser config()
2. **ALLOWED_HOSTS vide** - Doit contenir au moins localhost et 127.0.0.1
3. **CSRF_TRUSTED_ORIGINS manquant** - Necessaire pour les versions recentes de Django
4. **Sessions corrompues** - Anciennes sessions peuvent causer des problemes

## Solutions appliquees

### 1. Correction du fichier settings.py

#### Avant:
```python
SECRET_KEY ='5792c544-51e8-4b59-aaf2-d1880334587a'
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = []
```

#### Apres:
```python
SECRET_KEY = config('SECRET_KEY', default='5792c544-51e8-4b59-aaf2-d1880334587a')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# CSRF Configuration (ajoutee apres ROOT_URLCONF)
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
CSRF_COOKIE_SECURE = False  # Mettre True en production avec HTTPS
SESSION_COOKIE_SECURE = False  # Mettre True en production avec HTTPS
```

### 2. Nettoyage des sessions
```bash
python manage.py shell -c "from django.contrib.sessions.models import Session; Session.objects.all().delete()"
```

## Comment tester la correction

### Etape 1: Verifier la configuration
```bash
python manage.py check
```

### Etape 2: Creer un superutilisateur (si necessaire)
```bash
python manage.py createsuperuser
```
Exemple de credentials:
- Username: admin
- Email: admin@mokpokpo.com
- Password: Admin@123

### Etape 3: Lancer le serveur
```bash
python manage.py runserver
```

### Etape 4: Tester la connexion admin
1. Ouvrir le navigateur en mode incognito (pour eviter le cache)
2. Aller sur: http://127.0.0.1:8000/admin/
3. Se connecter avec les identifiants du superutilisateur

## Si le probleme persiste

### Solution 1: Vider le cache du navigateur
- **Chrome/Edge**: Ctrl + Shift + Delete
- **Firefox**: Ctrl + Shift + Delete
- Ou utiliser le mode navigation privee/incognito

### Solution 2: Verifier le middleware CSRF
Dans settings.py, verifier que cette ligne est presente:
```python
MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
```

### Solution 3: Verifier les templates
Tous les formulaires POST doivent contenir:
```html
<form method="post">
    {% csrf_token %}
    <!-- Champs du formulaire -->
</form>
```

### Solution 4: Regenerer la SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copier la nouvelle cle dans le fichier .env:
```
SECRET_KEY=nouvelle_cle_generee_ici
```

## Configuration du fichier .env

Votre fichier .env doit contenir:
```env
# Django
SECRET_KEY=5792c544-51e8-4b59-aaf2-d1880334587a
DEBUG=True

# Database
DB_NAME=mokpokpo_db
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

## Verification finale

Apres toutes les corrections, verifier:

1. **Settings.py** ?
   - SECRET_KEY correcte
   - DEBUG=True pour le developpement
   - ALLOWED_HOSTS configure
   - CSRF_TRUSTED_ORIGINS configure

2. **Database** ?
   - Migrations appliquees: `python manage.py migrate`
   - Superutilisateur cree: `python manage.py createsuperuser`

3. **Serveur** ?
   - Aucune erreur au demarrage
   - Accessible sur http://127.0.0.1:8000/

4. **Admin** ?
   - Page de connexion affichee correctement
   - Connexion reussie sans erreur CSRF

## Commandes utiles

```bash
# Verifier la configuration
python manage.py check

# Appliquer les migrations
python manage.py migrate

# Creer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver

# Nettoyer les sessions
python manage.py clearsessions

# Acceder au shell Django
python manage.py shell

# Collecter les fichiers statiques (pour production)
python manage.py collectstatic
```

## Notes de securite pour la production

Quand vous deployez en production, modifier dans settings.py:

```python
DEBUG = False
ALLOWED_HOSTS = ['votre-domaine.com', 'www.votre-domaine.com']
SECRET_KEY = config('SECRET_KEY')  # Utiliser une cle forte depuis .env

# CSRF et securite
CSRF_TRUSTED_ORIGINS = [
    'https://votre-domaine.com',
    'https://www.votre-domaine.com',
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
```

## Support

Si le probleme persiste apres toutes ces etapes:
1. Verifier les logs du serveur Django
2. Verifier les logs PostgreSQL
3. Tester avec un navigateur different
4. Verifier que le port 8000 n'est pas utilise par un autre processus
