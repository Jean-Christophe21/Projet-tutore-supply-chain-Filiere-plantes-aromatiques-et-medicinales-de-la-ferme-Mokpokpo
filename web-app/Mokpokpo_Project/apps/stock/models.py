from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from apps.products.models import Produit


STATUT_ALERTE_CHOICES = [
    ('ENVOYEE', 'Envoyee'),
    ('TRAITEE', 'Traitee'),
]


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    quantite_disponible = models.IntegerField(
        null=False,
        validators=[MinValueValidator(0)]
    )
    seuil_minimal = models.IntegerField(
        null=False,
        validators=[MinValueValidator(0)]
    )
    date_derniere_mise_a_jour = models.DateTimeField(default=timezone.now)
    id_produit = models.OneToOneField(
        Produit,
        on_delete=models.CASCADE,
        unique=True,
        related_name='stock',
        db_column='id_produit'
    )

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return f"Stock {self.id_produit.nom_produit}: {self.quantite_disponible} unites"

    def est_en_rupture(self):
        return self.quantite_disponible < self.seuil_minimal


class AlerteStock(models.Model):
    id_alerte = models.AutoField(primary_key=True)
    date_alerte = models.DateTimeField(default=timezone.now)
    message = models.TextField(null=False, blank=False)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_ALERTE_CHOICES,
        null=False,
        blank=False
    )
    seuil_declencheur = models.IntegerField(null=False)
    id_produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='alertes',
        db_column='id_produit'
    )

    class Meta:
        db_table = 'alerte_stock'
        verbose_name = 'Alerte Stock'
        verbose_name_plural = 'Alertes Stock'

    def __str__(self):
        return f"Alerte {self.id_produit.nom_produit} - {self.get_statut_display()}"

