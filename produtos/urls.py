from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('listar/', views.listar, name="listar"),
    path('excluir/', views.excluir, name="excluir_produto"),
    path('carregar_produto/', views.carregar_produto, name="carregar_produto"),
    path('atualizar_produto/', views.atualizar, name='atualizar_produto'),
]