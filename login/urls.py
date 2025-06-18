from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('lista', views.listar, name="listar"),
    path('cadastro', views.cadastrar, name="cadastrar"),
]