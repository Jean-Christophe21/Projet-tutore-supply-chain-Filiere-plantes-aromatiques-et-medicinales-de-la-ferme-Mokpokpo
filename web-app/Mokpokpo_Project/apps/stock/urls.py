from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    # Dashboard stock
    path('', views.stock_dashboard, name='dashboard'),
]
