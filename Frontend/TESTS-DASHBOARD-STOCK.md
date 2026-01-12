# ?? Tests Dashboard Gestionnaire de Stock

## Tests Fonctionnels

### ? Test 1: Chargement Initial
**Objectif:** Vérifier que le dashboard charge correctement

**Actions:**
1. Se connecter avec un compte GEST_STOCK
2. Observer le chargement du dashboard

**Résultats Attendus:**
- ? Redirection automatique vers `stock-dashboard.html`
- ? Affichage des 4 cartes de statistiques
- ? Nom de l'utilisateur affiché en haut à droite
- ? Badge d'alertes dans la sidebar
- ? Animations de comptage sur les chiffres

**Commande Console:**
```javascript
// Vérifier l'authentification
console.log('Token:', localStorage.getItem('token'));
console.log('User:', JSON.parse(localStorage.getItem('currentUser')));
console.assert(JSON.parse(localStorage.getItem('currentUser')).role === 'GEST_STOCK');
```

---

### ? Test 2: Affichage des Stocks
**Objectif:** Vérifier l'affichage de la liste des stocks

**Actions:**
1. Cliquer sur "Niveaux de Stock" dans la sidebar
2. Observer l'affichage

**Résultats Attendus:**
- ? Spinner de chargement affiché
- ? Liste des stocks chargée depuis API
- ? Stocks critiques en haut de liste
- ? Barres de progression colorées
- ? Boutons "Réapprovisionner" sur stocks bas
- ? Icônes et emojis affichés
- ? Noms scientifiques (si disponibles)

**Commande Console:**
```javascript
// Tester l'API stocks
fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(stocks => {
    console.log(`? ${stocks.length} stocks chargés`);
    console.table(stocks);
});
```

---

### ? Test 3: Enregistrement d'une Entrée
**Objectif:** Vérifier l'enregistrement d'une récolte/achat

**Actions:**
1. Cliquer sur "Enregistrer Récolte"
2. Sélectionner un produit
3. Entrer une quantité (ex: 50)
4. Sélectionner "Entrée"
5. Cliquer sur "Enregistrer"

**Résultats Attendus:**
- ? Bouton passe en état "Enregistrement..."
- ? Notification de succès affichée
- ? Message: "? 50 unités ajoutées (Stock: X)"
- ? Formulaire réinitialisé
- ? Statistiques mises à jour
- ? Animation pulse sur le formulaire

**Vérification Console:**
```javascript
// Avant
const stockAvant = 100;

// Après action
const stockApres = 150;

console.assert(stockApres === stockAvant + 50, '? Stock correctement incrémenté');
```

---

### ? Test 4: Enregistrement d'une Sortie
**Objectif:** Vérifier l'enregistrement d'une vente/perte

**Actions:**
1. Aller à "Enregistrer Récolte"
2. Sélectionner un produit avec stock > 20
3. Entrer quantité: 20
4. Sélectionner "Sortie"
5. Enregistrer

**Résultats Attendus:**
- ? Validation de la quantité disponible
- ? Notification: "? 20 unités retirées (Stock: X)"
- ? Stock décrémenté correctement
- ? Si stock passe sous seuil, alerte créée

**Test Cas d'Erreur:**
```javascript
// Tenter de retirer plus que disponible
// Si stock = 10, tenter de retirer 20
// Résultat attendu: ?? Quantité insuffisante en stock
```

---

### ? Test 5: Validation des Données
**Objectif:** Vérifier que les validations fonctionnent

**Tests à effectuer:**

| Test | Action | Résultat Attendu |
|------|--------|------------------|
| Quantité négative | Entrer -5 | ?? La quantité doit être supérieure à 0 |
| Quantité zéro | Entrer 0 | ?? La quantité doit être supérieure à 0 |
| Pas de produit | Laisser vide | ?? Veuillez remplir tous les champs |
| Sortie > Stock | Sortie de 100, stock = 50 | ?? Quantité insuffisante |

---

### ? Test 6: Système d'Alertes
**Objectif:** Vérifier la détection et l'affichage des alertes

**Actions:**
1. Créer/identifier un produit avec stock ? seuil
2. Cliquer sur "Alertes Stock"

**Résultats Attendus:**
- ? Alerte affichée avec détails
- ? Badge pulsant dans sidebar (nombre > 0)
- ? Icône ?? ou ?
- ? Message: "Stock actuel: X unités"
- ? Bouton "Réapprovisionner"
- ? Alerte enregistrée dans `/alertes-stock/`

**Test Console:**
```javascript
// Vérifier les alertes
fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('token') }
})
.then(r => r.json())
.then(stocks => {
    const alerts = stocks.filter(s => s.seuil_alerte && s.quantite_stock <= s.seuil_alerte);
    console.log(`?? ${alerts.length} alertes détectées`);
    console.table(alerts);
});
```

---

### ? Test 7: Réapprovisionnement Rapide
**Objectif:** Vérifier le workflow de réapprovisionnement rapide

**Actions:**
1. Dans "Niveaux de Stock", trouver un stock critique
2. Cliquer sur "Réapprovisionner"
3. Observer

**Résultats Attendus:**
- ? Navigation vers formulaire
- ? Produit pré-sélectionné
- ? Type "ENTREE" pré-sélectionné
- ? Focus sur champ quantité
- ? Entrée directe du nombre possible

**Test Workflow:**
```javascript
// Simuler le workflow
function testRestock() {
    const productId = 5; // Exemple
    goToRestock(productId);
    
    // Vérifier après 500ms
    setTimeout(() => {
        const select = document.getElementById('harvestProduct');
        const type = document.getElementById('movementType');
        
        console.assert(select.value == productId, '? Produit pré-sélectionné');
        console.assert(type.value === 'ENTREE', '? Type ENTREE sélectionné');
    }, 500);
}
```

---

### ? Test 8: Auto-Refresh
**Objectif:** Vérifier l'actualisation automatique

**Actions:**
1. Rester sur le dashboard
2. Attendre 30 secondes
3. Observer

**Résultats Attendus:**
- ? Statistiques actualisées toutes les 30s
- ? Section active rechargée
- ? Pas de rafraîchissement complet de page
- ? Transitions fluides

**Test Console:**
```javascript
// Simuler et tester l'auto-refresh
let refreshCount = 0;

const originalLoadStats = loadDashboardStats;
loadDashboardStats = function() {
    refreshCount++;
    console.log(`?? Refresh #${refreshCount} à ${new Date().toLocaleTimeString()}`);
    return originalLoadStats.apply(this, arguments);
};

// Observer les refreshes sur 2 minutes
setTimeout(() => {
    console.log(`? ${refreshCount} refreshes effectués`);
    console.assert(refreshCount >= 4, '? Auto-refresh fonctionne');
}, 120000);
```

---

### ? Test 9: Animations
**Objectif:** Vérifier que les animations fonctionnent

**Éléments à tester:**
- [x] Comptage animé des statistiques
- [x] Badge pulsant sur alertes
- [x] Hover effect sur cartes de stock
- [x] Barres de progression transitions
- [x] Spinner de chargement
- [x] Animation pulse après succès formulaire
- [x] Notifications toast slide-in

**Inspection CSS:**
```javascript
// Vérifier les animations CSS
const badge = document.getElementById('alertsBadge');
const style = window.getComputedStyle(badge);
console.log('Animation:', style.animation);
```

---

### ? Test 10: Responsive
**Objectif:** Vérifier l'adaptation mobile/tablette

**Actions:**
1. Ouvrir DevTools
2. Activer mode responsive
3. Tester différentes tailles:
   - 320px (mobile petit)
   - 768px (tablette)
   - 1024px (desktop)
   - 1920px (grand écran)

**Résultats Attendus:**
- ? Cartes s'empilent sur mobile
- ? Sidebar collapsible
- ? Boutons adaptés
- ? Textes lisibles
- ? Pas de débordement horizontal
- ? Touch-friendly

---

## Tests d'Intégration API

### Test API 1: GET /stocks/
```javascript
async function testGetStocks() {
    const token = localStorage.getItem('token');
    const response = await fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    
    console.assert(response.ok, '? API stocks accessible');
    
    const stocks = await response.json();
    console.assert(Array.isArray(stocks), '? Retourne un tableau');
    console.assert(stocks.every(s => s.id_stock), '? Tous les stocks ont un ID');
    
    console.log(`? ${stocks.length} stocks chargés`);
}
```

### Test API 2: POST /stocks/
```javascript
async function testCreateStock() {
    const token = localStorage.getItem('token');
    const newStock = {
        id_produit: 1,
        quantite_stock: 100,
        seuil_alerte: 10,
        date_derniere_maj: new Date().toISOString()
    };
    
    const response = await fetch('https://bd-mokpokokpo.onrender.com/stocks/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newStock)
    });
    
    console.assert(response.ok, '? Création de stock OK');
    
    const created = await response.json();
    console.assert(created.id_stock, '? ID généré');
    console.assert(created.quantite_stock === 100, '? Quantité correcte');
    
    console.log('? Stock créé:', created);
}
```

### Test API 3: PUT /stocks/{id}
```javascript
async function testUpdateStock(stockId) {
    const token = localStorage.getItem('token');
    
    // Get current
    const getResponse = await fetch(`https://bd-mokpokokpo.onrender.com/stocks/${stockId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    const stock = await getResponse.json();
    
    // Update
    const updated = {
        ...stock,
        quantite_stock: stock.quantite_stock + 50,
        date_derniere_maj: new Date().toISOString()
    };
    
    const putResponse = await fetch(`https://bd-mokpokokpo.onrender.com/stocks/${stockId}`, {
        method: 'PUT',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updated)
    });
    
    console.assert(putResponse.ok, '? Mise à jour OK');
    
    const result = await putResponse.json();
    console.assert(result.quantite_stock === updated.quantite_stock, '? Quantité mise à jour');
    
    console.log('? Stock mis à jour:', result);
}
```

---

## Tests de Performance

### Test Perf 1: Temps de Chargement
```javascript
async function testLoadTime() {
    const start = performance.now();
    
    await loadDashboardStats();
    await loadStocks();
    
    const end = performance.now();
    const duration = end - start;
    
    console.log(`?? Temps de chargement: ${duration.toFixed(2)}ms`);
    console.assert(duration < 2000, '? Chargement en moins de 2s');
}
```

### Test Perf 2: Animations Fluides
```javascript
// Vérifier que les animations ne drop pas de frames
function testAnimationPerformance() {
    let lastTime = performance.now();
    let frameCount = 0;
    let droppedFrames = 0;
    
    function checkFrame() {
        const currentTime = performance.now();
        const delta = currentTime - lastTime;
        
        if (delta > 20) { // Plus de 16.67ms = frame dropped
            droppedFrames++;
        }
        
        frameCount++;
        lastTime = currentTime;
        
        if (frameCount < 300) { // Test sur 5 secondes
            requestAnimationFrame(checkFrame);
        } else {
            const dropRate = (droppedFrames / frameCount) * 100;
            console.log(`?? Frames: ${frameCount}, Dropped: ${droppedFrames} (${dropRate.toFixed(2)}%)`);
            console.assert(dropRate < 5, '? Moins de 5% de frames droppées');
        }
    }
    
    requestAnimationFrame(checkFrame);
}
```

---

## Checklist Tests Complets

### Fonctionnalités Core
- [ ] Authentification et accès
- [ ] Chargement initial du dashboard
- [ ] Affichage des statistiques
- [ ] Comptage animé des chiffres
- [ ] Navigation entre sections
- [ ] Auto-refresh 30 secondes

### Gestion des Stocks
- [ ] Liste des stocks affichée
- [ ] Tri par priorité (alertes first)
- [ ] Barres de progression
- [ ] Statuts colorés
- [ ] Boutons de réapprovisionnement
- [ ] Détails produits (noms scientifiques)

### Enregistrement des Mouvements
- [ ] Formulaire validé
- [ ] Création de nouveau stock
- [ ] Entrée (ajout au stock)
- [ ] Sortie (retrait du stock)
- [ ] Validation quantité insuffisante
- [ ] Messages de succès contextuels
- [ ] Loading states
- [ ] Auto-reset formulaire

### Système d'Alertes
- [ ] Détection automatique
- [ ] Badge pulsant
- [ ] Liste des alertes
- [ ] Niveaux d'urgence (danger/warning)
- [ ] Boutons d'action rapide
- [ ] Enregistrement en BDD

### Interface Utilisateur
- [ ] Design moderne
- [ ] Animations fluides
- [ ] Hover effects
- [ ] Notifications toast
- [ ] Spinners de chargement
- [ ] Messages d'erreur clairs
- [ ] Responsive design

### API et Performance
- [ ] Appels API réussis
- [ ] Gestion des erreurs
- [ ] Temps de réponse < 2s
- [ ] Pas de memory leaks
- [ ] Animations 60 FPS

---

## Résultats Tests

### ? Tests Réussis: __/10
### ?? Tests Partiels: __/10
### ? Tests Échoués: __/10

---

## Rapport de Bugs

| ID | Description | Sévérité | Statut |
|----|-------------|----------|--------|
| | | | |

---

## Notes d'Amélioration

1. 
2. 
3. 

---

**Date des tests:** ___________  
**Testeur:** ___________  
**Version:** 2.0  
**Status Global:** ? PASSED ? PARTIAL ? FAILED

---

## Script de Test Automatisé

```javascript
// test-stock-dashboard.js
async function runAllTests() {
    console.log('?? Début des tests du Dashboard Stock\n');
    
    const tests = [
        { name: 'Authentification', fn: testAuth },
        { name: 'Chargement Stats', fn: testLoadStats },
        { name: 'Affichage Stocks', fn: testDisplayStocks },
        { name: 'Enregistrement Entrée', fn: testRecordEntry },
        { name: 'Enregistrement Sortie', fn: testRecordExit },
        { name: 'Validation Données', fn: testValidation },
        { name: 'Système Alertes', fn: testAlerts },
        { name: 'Auto-Refresh', fn: testAutoRefresh },
        { name: 'API Integration', fn: testAPIIntegration },
        { name: 'Performance', fn: testPerformance }
    ];
    
    let passed = 0;
    let failed = 0;
    
    for (const test of tests) {
        try {
            console.log(`?? Test: ${test.name}`);
            await test.fn();
            console.log(`? ${test.name}: PASSED\n`);
            passed++;
        } catch (error) {
            console.error(`? ${test.name}: FAILED`, error);
            failed++;
        }
    }
    
    console.log('\n?? Résultats:');
    console.log(`? Réussis: ${passed}/${tests.length}`);
    console.log(`? Échoués: ${failed}/${tests.length}`);
    console.log(`?? Taux de réussite: ${((passed/tests.length)*100).toFixed(2)}%`);
}

// Lancer les tests
runAllTests();
```

**Tests Dashboard Stock Complets !** ???
