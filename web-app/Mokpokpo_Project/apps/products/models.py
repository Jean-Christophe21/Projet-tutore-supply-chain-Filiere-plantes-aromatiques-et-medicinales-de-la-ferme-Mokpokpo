from django.db import models
from django.core.validators import MinValueValidator


class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=150, null=False, blank=False)
    type_produit = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    usages = models.TextField(null=True, blank=True)
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        db_table = 'produit'
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return f"{self.nom_produit} - {self.prix_unitaire} Euro"
