from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from apps.accounts.models import Client
from apps.products.models import Produit


STATUT_COMMANDE_CHOICES = [
    ('EN_ATTENTE', 'En attente'),
    ('ACCEPTEE', 'Acceptee'),
    ('REFUSEE', 'Refusee'),
]


class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.DateTimeField(default=timezone.now)
    montant_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    statut = models.CharField(
        max_length=20,
        choices=STATUT_COMMANDE_CHOICES,
        null=False,
        blank=False
    )
    id_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='commandes',
        db_column='id_client'
    )

    class Meta:
        db_table = 'commande'
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'
        ordering = ['-date_commande']

    def __str__(self):
        return f"Commande #{self.id_commande} - {self.get_statut_display()}"


class LigneCommande(models.Model):
    id_ligne_commande = models.AutoField(primary_key=True)
    quantite = models.IntegerField(
        null=False,
        validators=[MinValueValidator(1)]
    )
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        validators=[MinValueValidator(0)]
    )
    montant_ligne = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False
    )
    id_commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name='lignes',
        db_column='id_commande'
    )
    id_produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='lignes_commande',
        db_column='id_produit'
    )

    class Meta:
        db_table = 'ligne_commande'
        verbose_name = 'Ligne de commande'
        verbose_name_plural = 'Lignes de commande'

    def __str__(self):
        return f"{self.id_produit.nom_produit} x{self.quantite}"

    def save(self, *args, **kwargs):
        self.montant_ligne = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)


class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    date_reservation = models.DateTimeField(default=timezone.now)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_COMMANDE_CHOICES,
        null=False,
        blank=False
    )
    id_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reservations',
        db_column='id_client'
    )

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ['-date_reservation']

    def __str__(self):
        return f"Reservation #{self.id_reservation} - {self.get_statut_display()}"


class LigneReservation(models.Model):
    id_ligne_reservation = models.AutoField(primary_key=True)
    quantite_reservee = models.IntegerField(
        null=False,
        validators=[MinValueValidator(1)]
    )
    id_reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='lignes',
        db_column='id_reservation'
    )
    id_produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='lignes_reservation',
        db_column='id_produit'
    )

    class Meta:
        db_table = 'ligne_reservation'
        verbose_name = 'Ligne de reservation'
        verbose_name_plural = 'Lignes de reservation'

    def __str__(self):
        return f"{self.id_produit.nom_produit} x{self.quantite_reservee} (Reserve)"


class Vente(models.Model):
    id_vente = models.AutoField(primary_key=True)
    date_vente = models.DateTimeField(default=timezone.now)
    chiffre_affaires = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False
    )
    id_commande = models.OneToOneField(
        Commande,
        on_delete=models.CASCADE,
        unique=True,
        related_name='vente',
        db_column='id_commande'
    )

    class Meta:
        db_table = 'vente'
        verbose_name = 'Vente'
        verbose_name_plural = 'Ventes'
        ordering = ['-date_vente']

    def __str__(self):
        return f"Vente #{self.id_vente} - {self.chiffre_affaires} Euro"

