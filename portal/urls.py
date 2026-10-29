from django.urls import path
from . import views

urlpatterns = [
    # Página inicial: http://127.0.0.1:8000/
    path('', views.home, name='home'),
    
    # Página de conteúdo dinâmico: http://127.0.0.1:8000/conteudo/meu-tema/
    path('conteudo/<slug:slug>/', views.conteudo_detalhe, name='conteudo_detalhe'),
]