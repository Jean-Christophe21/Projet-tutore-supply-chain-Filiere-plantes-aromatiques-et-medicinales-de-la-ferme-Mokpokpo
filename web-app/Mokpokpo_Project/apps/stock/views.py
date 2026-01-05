from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def stock_dashboard(request):
    """Dashboard pour le gestionnaire de stock"""
    return render(request, 'dashboard/stock.html')

