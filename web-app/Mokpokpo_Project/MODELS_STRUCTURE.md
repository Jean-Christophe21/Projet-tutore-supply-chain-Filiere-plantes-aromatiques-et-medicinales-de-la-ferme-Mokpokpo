# Structure des Modeles Django - Projet Mokpokpo

Ce document recapitule la structure des modeles Django crees a partir du schema SQL PostgreSQL.

## 1. Application: accounts (apps/accounts/models.py)

### Modele: Utilisateur
- **Table**: utilisateur
- **Champs**:
  - id_utilisateur: AutoField (PK)
  - nom: CharField(100)
  - prenom: CharField(100)
  - email: EmailField(150, unique)
  - mot_de_passe: TextField
  - role: CharField(30) - Choix: CLIENT, GEST_COMMERCIAL, GEST_STOCK, ADMIN
  - date_creation: DateTimeField(auto_now_add)

### Modele: Client
- **Table**: client
- **Champs**:
  - id_client: AutoField (PK)
  - telephone: CharField(30, nullable)
  - adresse: TextField(nullable)
  - id_utilisateur: OneToOneField(Utilisateur, CASCADE)

---

## 2. Application: products (apps/products/models.py)

### Modele: Produit
- **Table**: produit
- **Champs**:
  - id_produit: AutoField (PK)
  - nom_produit: CharField(150)
  - type_produit: CharField(50, nullable)
  - description: TextField(nullable)
  - usages: TextField(nullable)
  - prix_unitaire: DecimalField(10,2) - Min: 0

---

## 3. Application: stock (apps/stock/models.py)

### Modele: Stock
- **Table**: stock
- **Champs**:
  - id_stock: AutoField (PK)
  - quantite_disponible: IntegerField - Min: 0
  - seuil_minimal: IntegerField - Min: 0
  - date_derniere_mise_a_jour: DateTimeField(auto_now)
  - id_produit: OneToOneField(Produit, CASCADE)
- **Methodes**:
  - est_en_rupture(): Verifie si stock < seuil_minimal

### Modele: AlerteStock
- **Table**: alerte_stock
- **Champs**:
  - id_alerte: AutoField (PK)
  - date_alerte: DateTimeField(auto_now_add)
  - message: TextField
  - statut: CharField(20) - Choix: ENVOYEE, TRAITEE
  - seuil_declencheur: IntegerField
  - id_produit: ForeignKey(Produit, CASCADE)

---

## 4. Application: sales (apps/sales/models.py)

### Modele: Commande
- **Table**: commande
- **Champs**:
  - id_commande: AutoField (PK)
  - date_commande: DateTimeField(auto_now_add)
  - montant_total: DecimalField(12,2)
  - statut: CharField(20) - Choix: EN_ATTENTE, ACCEPTEE, REFUSEE
  - id_client: ForeignKey(Client, CASCADE)

### Modele: LigneCommande
- **Table**: ligne_commande
- **Champs**:
  - id_ligne_commande: AutoField (PK)
  - quantite: IntegerField - Min: 1
  - prix_unitaire: DecimalField(10,2) - Min: 0
  - montant_ligne: DecimalField(12,2) - Calcule automatiquement
  - id_commande: ForeignKey(Commande, CASCADE)
  - id_produit: ForeignKey(Produit, CASCADE)
- **Methodes**:
  - save(): Calcule automatiquement montant_ligne = quantite * prix_unitaire

### Modele: Reservation
- **Table**: reservation
- **Champs**:
  - id_reservation: AutoField (PK)
  - date_reservation: DateTimeField(auto_now_add)
  - statut: CharField(20) - Choix: EN_ATTENTE, ACCEPTEE, REFUSEE
  - id_client: ForeignKey(Client, CASCADE)

### Modele: LigneReservation
- **Table**: ligne_reservation
- **Champs**:
  - id_ligne_reservation: AutoField (PK)
  - quantite_reservee: IntegerField - Min: 1
  - id_reservation: ForeignKey(Reservation, CASCADE)
  - id_produit: ForeignKey(Produit, CASCADE)

### Modele: Vente
- **Table**: vente
- **Champs**:
  - id_vente: AutoField (PK)
  - date_vente: DateTimeField(auto_now_add)
  - chiffre_affaires: DecimalField(12,2)
  - id_commande: OneToOneField(Commande, CASCADE)

---

## 5. Application: dashboard (apps/dashboard/models.py)

Aucun modele propre. Cette application utilise les modeles des autres applications
pour afficher des vues d'ensemble et des statistiques.

---

## Relations entre les modeles

```
Utilisateur (1) <--OneToOne--> (1) Client
                                    |
                                    | (1:N)
                                    v
                              Commande / Reservation
                                    |
                                    | (1:N)
                                    v
                         LigneCommande / LigneReservation
                                    |
                                    | (N:1)
                                    v
Produit (1) <--OneToOne--> (1) Stock
    |
    | (1:N)
    v
AlerteStock

Commande (1) <--OneToOne--> (1) Vente
```

---

## Commandes Django utiles

### Creer les migrations
```bash
python manage.py makemigrations
```

### Appliquer les migrations
```bash
python manage.py migrate
```

### Creer un superutilisateur
```bash
python manage.py createsuperuser
```

### Lancer le serveur
```bash
python manage.py runserver
```

---

## Notes importantes

1. **Encodage**: Tous les fichiers sont en UTF-8
2. **Validations**: Les contraintes CHECK de PostgreSQL sont implementees avec des validators Django
3. **Cascades**: Les suppressions en cascade (ON DELETE CASCADE) sont implementees avec on_delete=models.CASCADE
4. **Timestamps**: Les champs de date utilisent timezone.now pour etre timezone-aware
5. **Choices**: Les enums PostgreSQL sont implementes avec des tuples CHOICES
