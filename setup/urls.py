"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD

=======
>>>>>>> 8c53cf52987d34afb9ae9d704f6731c5f82cafa4
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD

    path('', TemplateView.as_view(template_name='pe_confortavel.html')),

    path('clientes/', include("clientes.urls", namespace='clientes')),
    path('contato/', include('contato.urls', namespace='contato')), 
    path('fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
    path('login/', include('login.urls', namespace='login')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('venda/', include('venda.urls', namespace='venda')),
]


=======
    path('', TemplateView.as_view(template_name='escola.html')),
    path('tiposdeatividades/', include('tiposdeatividades.urls', namespace='tiposdeatividades')),  
    path('aluno/', include('aluno.urls', namespace='aluno')),
    path('instrutor/', include('instrutor.urls', namespace='instrutor')),
    path('titulo/', include('titulo.urls', namespace='titulo')),
    path('turma/', include('turma.urls', namespace='turma')),
    path('utilitarios/', include('utilitarios.urls', namespace='contato')),  
    # path('contato/', include('contato.urls', namespace='contato')),
]
>>>>>>> 8c53cf52987d34afb9ae9d704f6731c5f82cafa4
