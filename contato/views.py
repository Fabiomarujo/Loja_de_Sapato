# from django.shortcuts import render

# # Create your views here.
# def listar(request):
#     return render(request, 'clientes/listarClientes.html')

# def cadastrar(request):
#     return render(request, 'clientes/cadastroClientes.html')
    

from django.shortcuts import render, redirect
from contato import utils

# Create your views here.
def contato(request):
    return render(request, 'contato/contato.html')

