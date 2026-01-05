cp# ACCES RAPIDE - Admin Django Mokpokpo

## ?? Demarrage rapide (3 etapes)

```bash
# 1. Demarrer le serveur
python manage.py runserver

# 2. Ouvrir le navigateur EN MODE PRIVE
# Chrome/Edge: Ctrl + Shift + N
# Firefox: Ctrl + Shift + P

# 3. Aller sur:
http://127.0.0.1:8000/admin/
```

## ?? Identifiants
- **Username**: `mokpokpo_user`
- **Password**: [Votre mot de passe]

## ? Commandes utiles

```bash
# Verifier la configuration
python check_config.py

# Verifier Django
python manage.py check

# Nettoyer les sessions
python manage.py clearsessions

# Changer le mot de passe
python manage.py changepassword mokpokpo_user

# Creer un superutilisateur
python manage.py createsuperuser
```

## ?? Fichiers importants

- **settings.py** ? Configuration principale ? CORRIGEE
- **.env** ? Variables d'environnement
- **INSTRUCTIONS_CONNEXION.md** ? Guide detaille
- **RESUME.md** ? Resume de toutes les corrections

## ? Ce qui a ete corrige

1. SECRET_KEY corrigee
2. ALLOWED_HOSTS configure
3. CSRF_TRUSTED_ORIGINS ajoute
4. Import incorrect dans admin.py corrige
5. Sessions nettoyees

## ?? Important

**Toujours utiliser le mode navigation privee du navigateur !**

Sinon, vider le cache:
- Chrome/Edge: `Ctrl + Shift + Delete`
- Firefox: `Ctrl + Shift + Delete`
