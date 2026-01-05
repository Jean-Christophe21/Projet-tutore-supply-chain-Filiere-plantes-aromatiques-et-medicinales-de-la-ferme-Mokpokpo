from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from .forms import CustomUserCreationForm
from .models import Utilisateur, Client


def register(request):
    """Vue d'inscription"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            
            # Creer un utilisateur Django pour l'authentification
            django_user = DjangoUser.objects.create_user(
                username=utilisateur.email,
                email=utilisateur.email,
                password=form.cleaned_data['password1'],
                first_name=utilisateur.prenom,
                last_name=utilisateur.nom
            )
            
            # Connecter automatiquement l'utilisateur
            auth_login(request, django_user)
            messages.success(request, 'Votre compte a ete cree avec succes !')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """Vue de connexion"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authentifier avec l'email comme username
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Bienvenue {user.first_name} !')
            
            # Redirection selon le role
            try:
                utilisateur = Utilisateur.objects.get(email=email)
                if utilisateur.role == 'ADMIN':
                    return redirect('/admin/')
                elif utilisateur.role == 'GEST_COMMERCIAL':
                    return redirect('dashboard:commercial')
                elif utilisateur.role == 'GEST_STOCK':
                    return redirect('dashboard:stock')
                else:
                    return redirect('home')
            except Utilisateur.DoesNotExist:
                return redirect('home')
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    """Vue de deconnexion"""
    auth_logout(request)
    messages.info(request, 'Vous avez ete deconnecte.')
    return redirect('home')


@login_required
def profile(request):
    """Vue du profil utilisateur"""
    try:
        utilisateur = Utilisateur.objects.get(email=request.user.email)
        try:
            client = Client.objects.get(id_utilisateur=utilisateur)
        except Client.DoesNotExist:
            client = None
    except Utilisateur.DoesNotExist:
        messages.error(request, 'Profil utilisateur introuvable.')
        return redirect('home')
    
    context = {
        'utilisateur': utilisateur,
        'client': client
    }
    return render(request, 'accounts/profile.html', context)

