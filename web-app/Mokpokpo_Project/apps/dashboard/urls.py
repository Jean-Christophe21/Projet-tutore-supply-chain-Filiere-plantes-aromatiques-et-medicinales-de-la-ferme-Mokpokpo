from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('commercial/', views.dashboard_commercial, name='commercial'),
    path('stock/', views.dashboard_stock, name='stock'),
    path('admin/', views.dashboard_admin, name='admin'),
]
