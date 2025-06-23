from django.urls import path
from . import views

app_name = 'venda'

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"), 
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('listar/', views.listar, name="listar"),
    path('excluir/', views.excluir, name="excluir_venda"),
    path('carregar_venda/', views.carregar_venda, name="carregar_venda"),
    path('atualizar_venda/', views.atualizar, name='atualizar_venda'),
]