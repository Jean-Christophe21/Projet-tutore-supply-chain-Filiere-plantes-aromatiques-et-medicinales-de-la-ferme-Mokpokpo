# TODO - Prochaines Étapes du Projet Mokpokpo

## ?? Priorité Haute

### Backend

- [ ] **Ajouter endpoints de mise à jour**
  - [ ] `PUT /commandes/{id}` - Mettre à jour le statut d'une commande
  - [ ] `PUT /produits/{id}` - Modifier un produit
  - [ ] `PUT /stocks/{id}` - Mettre à jour un stock
  - [ ] `PUT /utilisateurs/{id}` - Modifier un utilisateur

- [ ] **Ajouter endpoints de suppression**
  - [ ] `DELETE /produits/{id}` - Supprimer un produit
  - [ ] `DELETE /utilisateurs/{id}` - Supprimer un utilisateur

- [ ] **Endpoints spécialisés**
  - [ ] `GET /commandes/user/{id}` - Commandes d'un utilisateur spécifique
  - [ ] `GET /commandes/status/{status}` - Filtrer par statut
  - [ ] `GET /stocks/low` - Produits avec stock bas
  - [ ] `POST /commandes/{id}/accept` - Accepter une commande
  - [ ] `POST /commandes/{id}/reject` - Refuser une commande

### Frontend

- [ ] **Page de détail produit** (`/catalog/[id]/page.tsx`)
  - [ ] Charger les détails depuis l'API
  - [ ] Afficher le stock disponible
  - [ ] Bouton "Ajouter au panier"
  - [ ] Images du produit

- [ ] **Page panier** (`/cart/page.tsx`)
  - [ ] Afficher les articles du panier
  - [ ] Modifier les quantités
  - [ ] Supprimer des articles
  - [ ] Calculer le total
  - [ ] Bouton "Valider la commande"
  - [ ] Créer la commande via l'API

- [ ] **Dashboard Client** (`/client/page.tsx`)
  - [ ] Afficher les commandes de l'utilisateur
  - [ ] Filtrer par statut
  - [ ] Voir les détails d'une commande
  - [ ] Historique des achats

- [ ] **Dashboard Commercial** (`/commercial/page.tsx`)
  - [ ] Liste des commandes en attente
  - [ ] Accepter/refuser des commandes
  - [ ] Créer des ventes
  - [ ] Statistiques de ventes

- [ ] **Dashboard Stock** (`/stock/page.tsx`)
  - [ ] Liste des stocks avec alertes
  - [ ] Mettre à jour les stocks
  - [ ] Historique des mouvements
  - [ ] Gérer les alertes

- [ ] **Dashboard Admin** (`/admin/page.tsx`)
  - [ ] Vue globale du système
  - [ ] Gestion des utilisateurs
  - [ ] Gestion des produits
  - [ ] Statistiques complètes

## ?? Priorité Moyenne

### Backend

- [ ] **Système de notifications**
  - [ ] Notifier le gestionnaire de stock quand stock < seuil
  - [ ] Notifier le commercial quand nouvelle commande
  - [ ] Notifier le client quand commande acceptée/refusée

- [ ] **Amélioration de la sécurité**
  - [ ] Refresh tokens
  - [ ] Limitation de taux par IP
  - [ ] Logging des actions sensibles
  - [ ] Audit trail

- [ ] **Rapports et statistiques**
  - [ ] Endpoint pour rapports de ventes
  - [ ] Endpoint pour statistiques produits
  - [ ] Endpoint pour tendances

### Frontend

- [ ] **Améliorations UX**
  - [ ] Loading skeletons
  - [ ] Animations de transition
  - [ ] Messages de confirmation
  - [ ] Gestion des erreurs plus élégante

- [ ] **Recherche avancée**
  - [ ] Recherche par prix
  - [ ] Recherche par disponibilité
  - [ ] Tri (prix, nom, popularité)

- [ ] **Profil utilisateur**
  - [ ] Page de profil
  - [ ] Modifier ses informations
  - [ ] Changer son mot de passe
  - [ ] Historique complet

## ?? Priorité Basse

### Backend

- [ ] **Upload d'images**
  - [ ] Endpoint pour uploader des images de produits
  - [ ] Stockage des images (local ou cloud)
  - [ ] Thumbnails automatiques

- [ ] **Système de favoris**
  - [ ] Ajouter des produits en favoris
  - [ ] Liste de souhaits

- [ ] **Export de données**
  - [ ] Export CSV des commandes
  - [ ] Export PDF des factures
  - [ ] Export Excel des rapports

### Frontend

- [ ] **Mode sombre**
  - [ ] Toggle dark/light mode
  - [ ] Persistance de la préférence

- [ ] **Internationalisation**
  - [ ] Support français/anglais
  - [ ] Conversion de devises

- [ ] **Progressive Web App**
  - [ ] Service worker
  - [ ] Installation sur mobile
  - [ ] Notifications push

- [ ] **Accessibilité**
  - [ ] Support clavier complet
  - [ ] Screen reader friendly
  - [ ] WCAG 2.1 AA compliance

## ?? Optimisations Techniques

### Backend

- [ ] **Performance**
  - [ ] Mise en cache avec Redis
  - [ ] Pagination sur les listes
  - [ ] Optimisation des requêtes SQL
  - [ ] Index sur les colonnes fréquemment recherchées

- [ ] **Tests**
  - [ ] Tests unitaires (pytest)
  - [ ] Tests d'intégration
  - [ ] Tests de charge
  - [ ] Couverture de code > 80%

- [ ] **Documentation**
  - [ ] Docstrings complètes
  - [ ] Schémas OpenAPI enrichis
  - [ ] Guide de contribution

### Frontend

- [ ] **Performance**
  - [ ] Code splitting
  - [ ] Lazy loading des images
  - [ ] Optimisation des bundles
  - [ ] Server-side rendering

- [ ] **Tests**
  - [ ] Tests unitaires (Jest)
  - [ ] Tests de composants (React Testing Library)
  - [ ] Tests E2E (Playwright)

- [ ] **SEO**
  - [ ] Métadonnées dynamiques
  - [ ] Sitemap
  - [ ] Structured data

## ?? Fonctionnalités Avancées (Futur)

- [ ] **Application mobile**
  - [ ] React Native
  - [ ] iOS & Android

- [ ] **Système de paiement**
  - [ ] Intégration Stripe/PayPal
  - [ ] Paiement mobile money (MTN, Moov)

- [ ] **Livraison**
  - [ ] Tracking de livraison
  - [ ] Intégration avec services de livraison

- [ ] **Programme de fidélité**
  - [ ] Points de fidélité
  - [ ] Récompenses
  - [ ] Codes promo

- [ ] **Système de revues**
  - [ ] Avis clients sur produits
  - [ ] Notes
  - [ ] Photos clients

- [ ] **Intelligence Artificielle**
  - [ ] Recommandations de produits
  - [ ] Prédiction de la demande
  - [ ] Chatbot support client

## ?? Bugs Connus

- [ ] Aucun bug majeur identifié pour le moment

## ?? Idées en Vrac

- [ ] Newsletter par email
- [ ] Blog sur les plantes médicinales
- [ ] Vidéos de tutoriels
- [ ] Recettes et usages des plantes
- [ ] Partenariats avec autres fermes
- [ ] Marketplace pour d'autres producteurs
- [ ] API publique pour développeurs tiers
- [ ] Widget pour intégrer sur d'autres sites

---

## ?? Notes

- Prioriser les fonctionnalités selon les besoins métier
- Tester chaque feature avant de passer à la suivante
- Documenter au fur et à mesure
- Demander des retours utilisateurs régulièrement

**Dernière mise à jour**: 07/01/2026
