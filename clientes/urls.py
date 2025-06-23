from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('cadastro', views.cadastro, name="cadastro"), 
    path('cadastrar', views.cadastrar, name="cadastrar"),
    path('listar/', views.listar, name="listar"),
    path('excluir/<int:id>', views.excluir, name="excluir_clientes"),
    path('carregar_clientes/<int:id>', views.carregar_clientes, name="carregar_clientes"),
    path('atualizar_clientes/', views.atualizar, name='atualizar_clientes'),
]