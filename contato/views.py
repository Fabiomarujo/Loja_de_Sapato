from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'clientes/listarClientes.html')

def cadastrar(request):
    return render(request, 'clientes/cadastroClientes.html')
    
    