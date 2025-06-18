from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'fornecedor/listarFornecedor.html')

def cadastrar(request):
    return render(request, 'fornecedor/cadastroFornecedor.html')
    
    