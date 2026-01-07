# Application Web

Ce dossier contient l'application web du projet.

## Contenu
- Code source de l'application
- Configuration
- Dépendances
- Documentation technique

## Structure des applications dans le projet

Mokpokpo (Projet)
│
├── 1.  accounts/         🔐 Qui utilise le site ? 
├── 2. products/         🌿 Qu'est-ce qu'on vend ?
├── 3. orders/           🛒 Comment acheter ?
├── 4. stock/            📦 Combien en stock ?
├── 5. sales/            💰 Combien on a vendu ?
└── 6. dashboard/        📊 Vue d'ensemble


## 4️⃣ Les 6 applications de Mokpokpo expliquées {#mokpokpo-apps}

### **📊 Vue d'ensemble**

```
Mokpokpo (Projet)
│
├── 1.  accounts/         🔐 Qui utilise le site ? 
├── 2. products/         🌿 Qu'est-ce qu'on vend ?
├── 3. orders/           🛒 Comment acheter ?
├── 4. stock/            📦 Combien en stock ?
├── 5. sales/            💰 Combien on a vendu ?
└── 6. dashboard/        📊 Vue d'ensemble
```

---

### **🔐 Application 1 : `accounts/` - Gestion des utilisateurs**

#### **Rôle** : 
Gérer **QUI** utilise la plateforme et avec **QUELS DROITS**. 

#### **Responsabilités** :
- ✅ Inscription des nouveaux utilisateurs
- ✅ Connexion / Déconnexion
- ✅ Gestion des profils utilisateur
- ✅ Réinitialisation de mot de passe
- ✅ Attribution des rôles (Client, Commercial, Gestionnaire Stock, Admin)
- ✅ Permissions (qui peut faire quoi)

#### **Modèles principaux** :
```python
User
├── id
├── email
├── password (hashé)
├── role : CLIENT / COMMERCIAL / STOCK / ADMIN
├── nom
├── prenom
├── telephone
├── adresse
└── date_creation
```

#### **Exemples d'URLs** :
```
/accounts/register/          → Créer un compte
/accounts/login/             → Se connecter
/accounts/logout/            → Se déconnecter
/accounts/profile/           → Voir mon profil
/accounts/profile/edit/      → Modifier mon profil
/accounts/password-reset/    → Mot de passe oublié
```

#### **Pages (templates)** :
- `register.html` → Formulaire d'inscription
- `login.html` → Formulaire de connexion
- `profile.html` → Affichage du profil
- `profile_edit.html` → Modification du profil

#### **Pourquoi une app séparée ?** :
- Système d'authentification **complexe** et critique
- Utilisé par **TOUTES** les autres apps
- Peut être **réutilisé** dans d'autres projets
- Sécurité nécessite une **isolation**

---

### **🌿 Application 2 : `products/` - Catalogue des produits**

#### **Rôle** :
Gérer **QUOI** vendre (les plantes médicinales et aromatiques).

#### **Responsabilités** :
- ✅ Afficher le catalogue des produits (public)
- ✅ Afficher la fiche détaillée d'un produit
- ✅ Créer / Modifier / Supprimer un produit (admin)
- ✅ Filtrer par type (médicinale / aromatique)
- ✅ Recherche de produits
- ✅ Gérer les images des produits
- ✅ Afficher la disponibilité

#### **Modèles principaux** :
```python
Produit
├── id
├── nom :  "Basilic"
├── type_plante :  MEDICINALE / AROMATIQUE
├── description : "Le basilic est..."
├── usages : "Aide à la digestion..."
├── prix_unitaire : 5.50 €
├── seuil_minimal : 10 (alerte si stock < 10)
├── image : photo du produit
├── disponible : True / False
└── date_creation
```

#### **Exemples d'URLs** : 
```
/produits/                       → Liste tous les produits
/produits/5/                     → Détail du produit #5
/produits/medicinales/           → Filtre plantes médicinales
/produits/aromatiques/           → Filtre plantes aromatiques
/produits/recherche/? q=basilic   → Recherche
```

#### **Pages (templates)** :
- `catalog.html` → Grille de produits avec photos
- `product_detail.html` → Fiche complète d'un produit
- `product_form.html` → Formulaire d'ajout/modification (admin)

#### **Pourquoi une app séparée ?** :
- Logique métier **spécifique** aux produits
- Peut évoluer indépendamment (ajouter des catégories, des avis, etc.)
- Peut être réutilisée pour vendre **autre chose** (miel, fromages...)

---

### **🛒 Application 3 : `orders/` - Commandes et réservations**

#### **Rôle** :
Gérer **COMMENT** les clients achètent.

#### **Responsabilités** :
- ✅ Gérer le panier d'achat (session)
- ✅ Ajouter / Modifier / Supprimer des produits du panier
- ✅ Valider une commande
- ✅ Créer des réservations
- ✅ Afficher l'historique des commandes (client)
- ✅ Gérer les commandes (commercial :  accepter/refuser)
- ✅ Suivre l'état d'une commande

#### **Modèles principaux** :
```python
Commande
├── id
├── client → User
├── date_commande
├── montant_total
├── statut : EN_ATTENTE / ACCEPTEE / REFUSEE / PREPAREE / LIVREE
└── commentaire

LigneCommande (détail de chaque produit)
├── id
├── commande → Commande
├── produit → Produit
├── quantite :  3
├── prix_unitaire : 5.50 (au moment de l'achat)
└── montant_ligne :  16.50

Reservation
├── id
├── client → User
├── produit → Produit
├── quantite_reservee
├── date_reservation
└── statut
```

#### **Exemples d'URLs** :
```
/panier/                         → Voir le panier
/panier/ajouter/5/               → Ajouter produit #5
/panier/modifier/5/              → Changer la quantité
/panier/supprimer/5/             → Retirer du panier
/panier/valider/                 → Passer commande

/commandes/                      → Mes commandes
/commandes/12/                   → Détail commande #12
/commandes/confirmation/12/      → Page de confirmation

/commandes/gestion/              → Liste (commercial)
/commandes/accepter/12/          → Accepter commande #12
/commandes/refuser/12/           → Refuser commande #12

/reservations/                   → Mes réservations
/reservations/creer/             → Créer une réservation
```

#### **Pages (templates)** :
- `cart.html` → Panier avec liste des produits
- `checkout.html` → Page de validation de commande
- `order_confirmation.html` → "Merci, votre commande est enregistrée"
- `order_list.html` → Liste des commandes (client)
- `order_detail.html` → Détail d'une commande
- `order_manage.html` → Gestion des commandes (commercial)

#### **Pourquoi une app séparée ?** : 
- Logique complexe (panier en session, création de commandes multi-produits)
- Concerne **deux rôles** :  client ET commercial
- Interactions avec `products` (vérifier stock) et `accounts` (identifier le client)

---

### **📦 Application 4 : `stock/` - Gestion des stocks**

#### **Rôle** :
Gérer **COMBIEN** de produits sont disponibles.

#### **Responsabilités** :
- ✅ Afficher l'état du stock par produit
- ✅ Enregistrer les entrées de stock (récoltes)
- ✅ Enregistrer les sorties de stock (ventes, pertes)
- ✅ Historiser tous les mouvements
- ✅ Générer des alertes si stock < seuil minimal
- ✅ Dashboard pour le gestionnaire de stock
- ✅ Traçabilité (qui a fait quoi, quand)

#### **Modèles principaux** :
```python
Stock (état actuel)
├── id
├── produit → Produit (OneToOne)
├── quantite_disponible :  45
└── date_derniere_maj

MouvementStock (historique)
├── id
├── produit → Produit
├── type_mouvement : ENTREE / SORTIE
├── motif : RECOLTE / VENTE / AJUSTEMENT / PERTE
├── quantite :  +20 ou -5
├── utilisateur → User (qui a fait l'opération)
├── date_operation
└── commentaire :  "Récolte du 15 janvier"

AlerteStock (notifications)
├── id
├── produit → Produit
├── message : "Stock de Basilic en dessous du seuil (3 unités)"
├── statut : NOUVELLE / EN_COURS / RESOLUE
├── date_alerte
└── date_resolution
```

#### **Exemples d'URLs** :
```
/stock/                      → Dashboard stock (vue d'ensemble)
/stock/mouvements/           → Historique de tous les mouvements
/stock/entree/               → Enregistrer une entrée (récolte)
/stock/sortie/               → Enregistrer une sortie manuelle
/stock/alertes/              → Liste des alertes actives
/stock/alertes/3/resoudre/   → Marquer alerte #3 comme résolue
```

#### **Pages (templates)** :
- `stock_dashboard.html` → Tableau avec tous les produits et leurs stocks
- `mouvement_form.html` → Formulaire d'entrée/sortie
- `mouvement_list.html` → Historique des mouvements
- `alertes. html` → Liste des alertes avec statuts

#### **Pourquoi une app séparée ?** :
- Logique métier **spécifique** à la logistique
- Utilisée **uniquement** par le gestionnaire de stock
- Peut évoluer (ajout de fournisseurs, codes-barres, etc.)
- Traçabilité critique → isolation pour la sécurité

---

### **💰 Application 5 : `sales/` - Suivi des ventes**

#### **Rôle** : 
Gérer **COMBIEN** on a vendu et à **QUEL PRIX**.

#### **Responsabilités** : 
- ✅ Créer une vente quand une commande est acceptée
- ✅ Afficher les ventes par période (jour, semaine, mois)
- ✅ Calculer le chiffre d'affaires
- ✅ Statistiques par produit
- ✅ Statistiques par client
- ✅ Rapports pour le gestionnaire commercial

#### **Modèles principaux** :
```python
Vente
├── id
├── commande → Commande (OneToOne)
├── date_vente
├── chiffre_affaires :  27.50 €
└── client → User (dénormalisé pour les stats)
```

#### **Exemples d'URLs** :
```
/ventes/                     → Dashboard ventes
/ventes/rapport/             → Rapport détaillé par période
/ventes/statistiques/        → Graphiques (optionnel MVP)
```

#### **Pages (templates)** :
- `sales_dashboard.html` → Vue d'ensemble des ventes
- `sales_report.html` → Tableau détaillé avec filtres de date
- `sales_stats.html` → Graphiques (si MVP avancé)

#### **Pourquoi une app séparée ? ** :
- Utilisée **uniquement** par le gestionnaire commercial
- Logique analytique différente des commandes
- Peut évoluer vers un système de prédiction (IA) sans toucher `orders`

---

### **📊 Application 6 : `dashboard/` - Tableaux de bord**

#### **Rôle** : 
Fournir une **vue d'ensemble** adaptée à chaque rôle.

#### **Responsabilités** :
- ✅ Rediriger chaque utilisateur vers son dashboard approprié
- ✅ Dashboard client : mes dernières commandes, mes réservations
- ✅ Dashboard commercial : commandes en attente, ventes du jour
- ✅ Dashboard gestionnaire stock : alertes, derniers mouvements
- ✅ Dashboard admin : vue globale du système

#### **Modèles principaux** :
```
Aucun modèle propre → Utilise les données des autres apps
```

#### **Exemples d'URLs** : 
```
/dashboard/                  → Redirection automatique selon le rôle
/dashboard/client/           → Dashboard client
/dashboard/commercial/       → Dashboard commercial
/dashboard/stock/            → Dashboard gestionnaire stock
/dashboard/admin/            → Dashboard administrateur
```

#### **Pages (templates)** :
- `client_dashboard.html` → Widgets :  dernières commandes, bouton "Commander"
- `commercial_dashboard.html` → Commandes en attente, ventes du jour
- `stock_dashboard.html` → Alertes stock, mouvements récents
- `admin_dashboard.html` → Vue globale :  nb utilisateurs, nb commandes, CA

#### **Pourquoi une app séparée ?** : 
- **Centralise** les vues d'ensemble
- Évite de dupliquer le code de redirection dans chaque app
- Peut évoluer (ajout de widgets, personnalisation)

---

## 5️⃣ Comment savoir si quelque chose doit être une app ?  {#quand-creer}

### **✅ Créez une app SI** :

```
✅ La fonctionnalité a un sens "seule"
   → Exemple : "Gestion des produits" peut exister sans "Commandes"

✅ Vous pouvez décrire sa responsabilité en UNE phrase
   → "Cette app gère l'authentification des utilisateurs"

✅ Elle pourrait être réutilisée dans un autre projet
   → Système d'auth, catalogue produits, système de panier

✅ Elle concerne un acteur/rôle spécifique
   → "stock" est utilisé uniquement par le gestionnaire de stock

✅ Elle a son propre cycle de vie de données
   → Produit :  créé → modifié → archivé
   → Commande : créée → validée → livrée
```