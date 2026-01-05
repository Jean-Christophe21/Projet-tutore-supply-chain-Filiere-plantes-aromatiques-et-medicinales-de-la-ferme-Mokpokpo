from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_commercial(request):
    """Dashboard pour le gestionnaire commercial"""
    return render(request, 'dashboard/commercial.html')


@login_required
def dashboard_stock(request):
    """Dashboard pour le gestionnaire de stock"""
    return render(request, 'dashboard/stock.html')


@login_required
def dashboard_admin(request):
    """Dashboard pour l'administrateur"""
    return render(request, 'dashboard/admin.html')

