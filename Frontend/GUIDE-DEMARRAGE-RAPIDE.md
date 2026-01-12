# ?? Guide de Démarrage Rapide - Dashboards Mokpokpo

## ?? Objectif

Ce guide vous permet de tester rapidement les dashboards améliorés pour les gestionnaires de Mokpokpo.

---

## ? Démarrage en 5 Minutes

### 1. Ouvrir l'Application

```bash
# Naviguez vers le dossier Frontend
cd Frontend

# Ouvrez index.html dans votre navigateur
# Ou lancez un serveur local:
python -m http.server 8000
# Puis ouvrez http://localhost:8000
```

### 2. Connexion

**Pour tester le Dashboard Commercial:**
```
Email: commercial@mokpokpo.com
Mot de passe: (votre mot de passe)
Rôle requis: GEST_COMMERCIAL
```

**Pour tester le Dashboard Stock:**
```
Email: stock@mokpokpo.com
Mot de passe: (votre mot de passe)
Rôle requis: GEST_STOCK
```

### 3. Exploration

**Dashboard Commercial:**
1. Observez les statistiques animées
2. Consultez l'activité récente
3. Testez la gestion des prix
4. Acceptez/Refusez une commande
5. Gérez une réservation

**Dashboard Stock:**
1. Vérifiez le badge d'alertes
2. Consultez les niveaux de stock
3. Enregistrez une entrée de stock
4. Testez le réapprovisionnement rapide
5. Consultez les alertes

---

## ?? Structure des Fichiers

```
Frontend/
??? index.html                          # Page d'accueil
??? login.html                          # Page de connexion
??? commercial-dashboard.html           # Dashboard commercial
??? stock-dashboard.html                # Dashboard stock
?
??? js/
?   ??? script.js                       # Fonctions communes
?   ??? commercial-dashboard.js         # Logique commercial
?   ??? stock-dashboard.js              # Logique stock
?
??? css/
?   ??? style.css                       # Styles (amélioré)
?
??? docs/
    ??? AMELIORATIONS-DASHBOARD-COMMERCIAL.md
    ??? AMELIORATIONS-DASHBOARD-STOCK.md
    ??? TESTS-DASHBOARD-STOCK.md
    ??? RECAP-DASHBOARDS.md
```

---

## ?? Configuration

### API Backend

L'URL de l'API est configurée dans les fichiers JS:

```javascript
const API_URL = 'https://bd-mokpokokpo.onrender.com';
```

Si vous utilisez un backend local:

```javascript
const API_URL = 'http://localhost:8000';  // Modifier selon votre config
```

### Authentification

Le système utilise JWT tokens stockés dans `localStorage`:

```javascript
// Token d'authentification
localStorage.getItem('token')

// Informations utilisateur
localStorage.getItem('currentUser')
```

---

## ?? Tests Rapides

### Test 1: Dashboard Commercial

```javascript
// Ouvrir la console du navigateur (F12)

// Vérifier l'authentification
console.log('Token:', localStorage.getItem('token'));
console.log('User:', JSON.parse(localStorage.getItem('currentUser')));

// Tester l'API produits
fetch('https://bd-mokpokokpo.onrender.com/produits/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(data => console.log('Produits:', data));

// Tester l'API commandes
fetch('https://bd-mokpokokpo.onrender.com/commandes/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(data => console.log('Commandes:', data));
```

### Test 2: Dashboard Stock

```javascript
// Tester l'API stocks
fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(data => console.log('Stocks:', data));

// Vérifier les alertes
fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(stocks => {
    const alerts = stocks.filter(s => s.seuil_alerte && s.quantite_stock <= s.seuil_alerte);
    console.log(`?? ${alerts.length} alertes détectées`);
});
```

---

## ? Checklist de Vérification

### Dashboard Commercial

- [ ] Page charge correctement
- [ ] Statistiques affichées avec animation
- [ ] Activité récente chargée
- [ ] Badge de commandes fonctionne
- [ ] Gestion des prix opérationnelle
- [ ] Acceptation/Refus de commandes fonctionne
- [ ] Réservations gérables
- [ ] Auto-refresh toutes les 30s

### Dashboard Stock

- [ ] Page charge correctement
- [ ] Statistiques affichées avec animation
- [ ] Badge d'alertes fonctionne
- [ ] Liste des stocks affichée
- [ ] Enregistrement d'entrée fonctionne
- [ ] Enregistrement de sortie fonctionne
- [ ] Alertes affichées correctement
- [ ] Réapprovisionnement rapide opérationnel

---

## ?? Dépannage Rapide

### Problème: "Token non trouvé"

**Solution:**
```javascript
// Se reconnecter via login.html
// Ou définir manuellement un token de test:
localStorage.setItem('token', 'VOTRE_TOKEN_JWT');
localStorage.setItem('currentUser', JSON.stringify({
    id_utilisateur: 1,
    prenom: 'Test',
    role: 'GEST_COMMERCIAL' // ou 'GEST_STOCK'
}));
```

### Problème: "Erreur CORS"

**Solution:**
- Vérifier que le backend autorise les requêtes depuis votre origine
- Utiliser un serveur local au lieu d'ouvrir directement le fichier HTML
- Vérifier la configuration CORS du backend

### Problème: "Données ne chargent pas"

**Solution:**
1. Ouvrir la console (F12)
2. Vérifier les erreurs réseau
3. Tester l'API manuellement:
```javascript
fetch('https://bd-mokpokokpo.onrender.com/produits/')
.then(r => console.log('Status:', r.status))
.then(r => r.json())
.then(console.log);
```

### Problème: "Animations ne fonctionnent pas"

**Solution:**
- Vérifier que `style.css` est bien chargé
- Vérifier la console pour des erreurs CSS
- Tester dans un autre navigateur

---

## ?? Données de Test

### Créer des Données de Test

**Produits:**
```javascript
// POST /produits/
{
    "nom_produit": "Aloe Vera",
    "nom_scientifique": "Aloe barbadensis",
    "prix_unitaire": 5000,
    "description": "Plante médicinale"
}
```

**Stock:**
```javascript
// POST /stocks/
{
    "id_produit": 1,
    "quantite_stock": 100,
    "seuil_alerte": 10
}
```

**Commande:**
```javascript
// POST /commandes/
{
    "id_utilisateur": 1,
    "statut": "EN_ATTENTE",
    "montant_total": 50000
}
```

---

## ?? Scénarios de Test

### Scénario 1: Workflow Commercial Complet

```
1. Connexion en tant que GEST_COMMERCIAL
2. Consulter statistiques (4 cartes)
3. Voir activité récente
4. Modifier un prix:
   - Aller à "Gestion des Prix"
   - Modifier le prix d'un produit
   - Enregistrer
   - Vérifier la notification
5. Gérer une commande:
   - Aller à "Commandes"
   - Trouver une commande EN_ATTENTE
   - Cliquer sur "Accepter"
   - Confirmer
   - Vérifier la mise à jour
6. Consulter les ventes:
   - Aller à "Statistiques"
   - Sélectionner période
   - Cliquer "Rechercher"
   - Observer les résultats
```

### Scénario 2: Workflow Stock Complet

```
1. Connexion en tant que GEST_STOCK
2. Consulter statistiques (4 cartes)
3. Vérifier badge d'alertes
4. Consulter stocks:
   - Aller à "Niveaux de Stock"
   - Observer le tri (alertes en haut)
   - Identifier stock critique
5. Réapprovisionner:
   - Cliquer sur "Réapprovisionner" sur stock bas
   - Observer navigation automatique
   - Entrer quantité: 100
   - Enregistrer
   - Vérifier notification
6. Consulter alertes:
   - Aller à "Alertes Stock"
   - Observer que l'alerte a disparu si stock > seuil
7. Enregistrer une sortie:
   - Aller à "Enregistrer Récolte"
   - Sélectionner produit
   - Type: "Sortie"
   - Quantité: 50
   - Enregistrer
   - Vérifier mise à jour
```

---

## ?? Test Responsive

### Test Mobile

```
1. Ouvrir DevTools (F12)
2. Clic sur l'icône de device toggle (Ctrl+Shift+M)
3. Sélectionner "iPhone 12 Pro"
4. Tester la navigation
5. Vérifier que:
   - Sidebar est collapsible
   - Cartes s'empilent verticalement
   - Boutons sont tactiles (pas trop petits)
   - Textes sont lisibles
```

### Test Tablette

```
1. DevTools > Device toggle
2. Sélectionner "iPad"
3. Vérifier que:
   - Layout adaptatif (2 colonnes)
   - Sidebar visible
   - Cartes bien proportionnées
```

---

## ? Performance

### Tester la Performance

```javascript
// Test de temps de chargement
const start = performance.now();

loadDashboardStats().then(() => {
    const end = performance.now();
    console.log(`?? Chargement: ${(end - start).toFixed(2)}ms`);
    console.assert(end - start < 2000, '? Chargement < 2s');
});

// Test d'auto-refresh
let refreshCount = 0;
const originalLoad = loadDashboardStats;
loadDashboardStats = function() {
    refreshCount++;
    console.log(`?? Refresh #${refreshCount}`);
    return originalLoad.apply(this, arguments);
};
```

---

## ?? Personnalisation

### Changer les Couleurs

**Commercial (Bleu ? Vert):**
```css
/* Dans style.css */
:root {
    --commercial-primary: #10b981;  /* Au lieu de #3b82f6 */
}
```

**Stock (Vert ? Bleu):**
```css
:root {
    --stock-primary: #3b82f6;  /* Au lieu de #10b981 */
}
```

### Modifier l'Auto-Refresh

```javascript
// Dans commercial-dashboard.js ou stock-dashboard.js

// Changer de 30s à 60s:
setInterval(() => {
    loadDashboardStats();
}, 60000); // 60000ms = 60s
```

---

## ?? Documentation Complète

Pour plus de détails, consultez:

- **Commercial:** `AMELIORATIONS-DASHBOARD-COMMERCIAL.md`
- **Stock:** `AMELIORATIONS-DASHBOARD-STOCK.md`
- **Tests:** `TESTS-DASHBOARD-STOCK.md`
- **Récapitulatif:** `RECAP-DASHBOARDS.md`

---

## ?? Prochaines Étapes

1. ? Testez les dashboards localement
2. ? Vérifiez toutes les fonctionnalités
3. ? Testez sur mobile/tablette
4. ? Vérifiez la performance
5. ? Déployez en production
6. ? Formez les utilisateurs
7. ? Collectez les retours
8. ? Itérez et améliorez

---

## ?? Support

**Besoin d'aide?**

- ?? Email: support@mokpokpo.com
- ?? Documentation: `/docs/`
- ?? Chat: (à venir)
- ?? Issues: GitHub Issues

---

## ?? Félicitations !

Vous êtes prêt à utiliser les dashboards améliorés de Mokpokpo ! ??

**Bon test et bonne gestion !** ??????

---

**Version:** 2.0  
**Date:** 12 Janvier 2025  
**Status:** ? PRÊT POUR TESTS

---

## ?? Commandes Utiles

```bash
# Lancer serveur local Python
python -m http.server 8000

# Lancer serveur local Node.js
npx http-server -p 8000

# Lancer serveur local PHP
php -S localhost:8000

# Ouvrir avec Live Server (VS Code)
# Clic droit sur index.html > "Open with Live Server"
```

---

**GUIDE COMPLET - PRÊT À UTILISER !** ?????
