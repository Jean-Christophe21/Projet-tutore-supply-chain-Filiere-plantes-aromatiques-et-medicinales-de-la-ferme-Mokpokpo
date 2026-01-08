# -*- coding: utf-8 -*-
"""
Script pour creer des donnees de test dans la base de donnees.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from database import engine, get_db
from models.model import Utilisateur, Client, Produit, Stock, Commande, LigneCommande
from security.hashing import hash_password
from decimal import Decimal

def create_test_data():
    db = next(get_db())
    
    try:
        print("Creation des utilisateurs...")
        
        admin = Utilisateur(
            nom="Admin",
            prenom="Super",
            email="admin@mokpokpo.com",
            mot_de_passe=hash_password("admin123"),
            role="ADMIN"
        )
        db.add(admin)
        
        commercial = Utilisateur(
            nom="Commercial",
            prenom="Jean",
            email="commercial@mokpokpo.com",
            mot_de_passe=hash_password("commercial123"),
            role="GEST_COMMERCIAL"
        )
        db.add(commercial)
        
        stock_manager = Utilisateur(
            nom="Stock",
            prenom="Marie",
            email="stock@mokpokpo.com",
            mot_de_passe=hash_password("stock123"),
            role="GEST_STOCK"
        )
        db.add(stock_manager)
        
        client1 = Utilisateur(
            nom="Dupont",
            prenom="Pierre",
            email="pierre.dupont@example.com",
            mot_de_passe=hash_password("client123"),
            role="CLIENT"
        )
        db.add(client1)
        
        client2 = Utilisateur(
            nom="Martin",
            prenom="Sophie",
            email="sophie.martin@example.com",
            mot_de_passe=hash_password("client123"),
            role="CLIENT"
        )
        db.add(client2)
        
        db.commit()
        print(f"OK - {5} utilisateurs crees")
        
        print("Creation des profils clients...")
        
        client_profile1 = Client(
            id_utilisateur=client1.id_utilisateur,
            telephone="+229 97 00 00 01",
            adresse="Cotonou, Benin"
        )
        db.add(client_profile1)
        
        client_profile2 = Client(
            id_utilisateur=client2.id_utilisateur,
            telephone="+229 97 00 00 02",
            adresse="Porto-Novo, Benin"
        )
        db.add(client_profile2)
        
        db.commit()
        print(f"OK - {2} profils clients crees")
        
        print("Creation des produits...")
        
        produits = [
            {
                "nom_produit": "Basilic Sacre",
                "type_produit": "MEDICINALE",
                "description": "Plante medicinale adaptogene",
                "usages": "Infusions, decoctions",
                "prix_unitaire": Decimal("2500.00")
            },
            {
                "nom_produit": "Aloe Vera",
                "type_produit": "MEDICINALE",
                "description": "Plante grasse aux multiples vertus",
                "usages": "Soins de la peau, digestion",
                "prix_unitaire": Decimal("3500.00")
            },
            {
                "nom_produit": "Moringa",
                "type_produit": "MEDICINALE",
                "description": "Arbre miracle riche en nutriments",
                "usages": "Poudre nutritionnelle, infusions",
                "prix_unitaire": Decimal("4000.00")
            },
            {
                "nom_produit": "Gingembre",
                "type_produit": "MEDICINALE",
                "description": "Rhizome anti-inflammatoire",
                "usages": "Cuisine, tisanes",
                "prix_unitaire": Decimal("3000.00")
            },
            {
                "nom_produit": "Menthe Poivree",
                "type_produit": "AROMATIQUE",
                "description": "Herbe aromatique fraiche",
                "usages": "Infusions, cuisine",
                "prix_unitaire": Decimal("1500.00")
            },
            {
                "nom_produit": "Basilic",
                "type_produit": "AROMATIQUE",
                "description": "Herbe aromatique essentielle",
                "usages": "Cuisine, pesto, sauces",
                "prix_unitaire": Decimal("2000.00")
            },
            {
                "nom_produit": "Coriandre",
                "type_produit": "AROMATIQUE",
                "description": "Herbe fraiche au gout unique",
                "usages": "Cuisine asiatique, garniture",
                "prix_unitaire": Decimal("1800.00")
            },
            {
                "nom_produit": "Thym",
                "type_produit": "AROMATIQUE",
                "description": "Herbe antiseptique",
                "usages": "Cuisine, infusions",
                "prix_unitaire": Decimal("2200.00")
            },
        ]
        
        produit_objs = []
        for p in produits:
            produit = Produit(**p)
            db.add(produit)
            produit_objs.append(produit)
        
        db.commit()
        print(f"OK - {len(produits)} produits crees")
        
        print("Creation des stocks...")
        
        stocks_data = [
            {"quantite": 50, "seuil": 10},
            {"quantite": 30, "seuil": 5},
            {"quantite": 100, "seuil": 20},
            {"quantite": 75, "seuil": 15},
            {"quantite": 60, "seuil": 10},
            {"quantite": 45, "seuil": 10},
            {"quantite": 8, "seuil": 10},
            {"quantite": 40, "seuil": 10},
        ]
        
        for produit, stock_data in zip(produit_objs, stocks_data):
            stock = Stock(
                quantite_disponible=stock_data["quantite"],
                seuil_minimal=stock_data["seuil"],
                id_produit=produit.id_produit
            )
            db.add(stock)
        
        db.commit()
        print(f"OK - {len(stocks_data)} stocks crees")
        
        print("Creation d'une commande exemple...")
        
        commande = Commande(
            statut="EN_ATTENTE",
            montant_total=Decimal("0"),
            id_utilisateur=client1.id_utilisateur
        )
        db.add(commande)
        db.commit()
        
        ligne1 = LigneCommande(
            quantite=2,
            prix_unitaire=produit_objs[0].prix_unitaire,
            montant_ligne=Decimal("5000.00"),
            id_commande=commande.id_commande,
            id_produit=produit_objs[0].id_produit
        )
        db.add(ligne1)
        
        ligne2 = LigneCommande(
            quantite=1,
            prix_unitaire=produit_objs[4].prix_unitaire,
            montant_ligne=Decimal("1500.00"),
            id_commande=commande.id_commande,
            id_produit=produit_objs[4].id_produit
        )
        db.add(ligne2)
        
        commande.montant_total = Decimal("6500.00")
        
        db.commit()
        print(f"OK - 1 commande creee avec 2 lignes")
        
        print("\n" + "="*60)
        print("DONNEES DE TEST CREEES AVEC SUCCES!")
        print("="*60)
        print("\nCOMPTES DE TEST:")
        print("-" * 60)
        print("Admin: admin@mokpokpo.com / admin123")
        print("Commercial: commercial@mokpokpo.com / commercial123")
        print("Stock: stock@mokpokpo.com / stock123")
        print("Client 1: pierre.dupont@example.com / client123")
        print("Client 2: sophie.martin@example.com / client123")
        print("-" * 60)
        print(f"\n{len(produits)} produits crees avec leur stock")
        print("1 commande exemple creee")
        print("="*60)
        
    except Exception as e:
        print(f"Erreur: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("\nCreation des donnees de test pour Mokpokpo...\n")
    create_test_data()

