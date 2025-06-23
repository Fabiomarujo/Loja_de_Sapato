from django.urls import path
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"), 
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('listar/', views.listar, name="listar"),
    path('excluir/', views.excluir, name="excluir_fornecedor"),
    path('carregar_fornecedor/', views.carregar_fornecedor, name="carregar_fornecedor"),
    path('atualizar_fornecedor/', views.atualizar, name='atualizar_fornecedor'),
]