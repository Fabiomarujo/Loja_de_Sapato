from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'produtos/listarProdutos.html')

def cadastrar(request):
    return render(request, 'produtos/cadastroProduto.html')
    
    