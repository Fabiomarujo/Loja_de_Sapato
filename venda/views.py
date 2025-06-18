from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'venda/listarVenda.html')

def cadastrar(request):
    return render(request, 'venda/cadastroVenda.html')
    
    