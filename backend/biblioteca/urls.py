from django.urls import path, include
from django.contrib import admin  # Importa o módulo admin do Django
from .routers import urlpatterns as api_patterns  # Importa as rotas do routers.py
from .views import index  # Importa a view index para testes de backend

urlpatterns = [
    path('', index),  # Rota para a raiz do servidor
    path('api/', include(api_patterns)),  # Inclui as rotas da API
    path('admin/', admin.site.urls),  # Rota para a interface administrativa
]
