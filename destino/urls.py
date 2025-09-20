from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atracoes/', views.atracoes, name='atracoes'),
    path('historia/', views.historia, name='historia'),
    path('galeria/', views.galeria, name='galeria'),
]
