from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User as DjangoUser
from .models import Utilisateur, Client


class CustomUserCreationForm(forms.ModelForm):
    """Formulaire d'inscription personnalise pour le modele Utilisateur"""
    
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )
    password2 = forms.CharField(
        label='Confirmation du mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez le mot de passe'})
    )
    
    telephone = forms.CharField(
        max_length=30,
        required=False,
        label='Telephone',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de telephone'})
    )
    
    adresse = forms.CharField(
        required=False,
        label='Adresse',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre adresse', 'rows': 3})
    )
    
    class Meta:
        model = Utilisateur
        fields = ('nom', 'prenom', 'email', 'telephone', 'adresse')
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prenom',
            'email': 'Email',
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Les mots de passe ne correspondent pas.')
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(email=email).exists():
            raise forms.ValidationError('Cet email est deja utilise.')
        return email
    
    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        utilisateur.mot_de_passe = self.cleaned_data['password1']
        utilisateur.role = 'CLIENT'  # Par defaut, nouveau compte = CLIENT
        
        if commit:
            utilisateur.save()
            
            # Creer le profil Client automatiquement
            Client.objects.create(
                id_utilisateur=utilisateur,
                telephone=self.cleaned_data.get('telephone', ''),
                adresse=self.cleaned_data.get('adresse', '')
            )
        
        return utilisateur


class CustomAuthenticationForm(AuthenticationForm):
    """Formulaire de connexion personnalise"""
    
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )
