from django.db import models
from django.utils import timezone

ROLE_CHOICES = [
    ('CLIENT', 'Client'),
    ('GEST_COMMERCIAL', 'Gestionnaire Commercial'),
    ('GEST_STOCK', 'Gestionnaire Stock'),
    ('ADMIN', 'Administrateur'),
]


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=False, blank=False)
    prenom = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, unique=True, null=False, blank=False)
    mot_de_passe = models.TextField(null=False, blank=False)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, null=False, blank=False)
    date_creation = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'utilisateur'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.get_role_display()})"


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    id_utilisateur = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        unique=True,
        related_name='client',
        db_column='id_utilisateur'
    )

    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"Client: {self.id_utilisateur.prenom} {self.id_utilisateur.nom}"
