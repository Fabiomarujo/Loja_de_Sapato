from django.shortcuts import render, redirect
from fornecedor.forms import FornecedorForm, FornecedorAtualizarForm
from fornecedor.models import Fornecedor

def listar(request):
    listar_fornecedor = Fornecedor.objects.all()
    contexto = {
        'fornecedor': listar_fornecedor,
    }
    return render(request, 'fornecedores/listarFornecedor.html', context=contexto)

def cadastro(request):
    return render(request, 'fornecedores/cadastroFornecedor.html')

def cadastrar(request):
    form = FornecedorForm(request.POST)
    if form.is_valid():
        dados_fornecedor = form.cleaned_data       
        fornecedor = Fornecedor(
            codigo=dados_fornecedor['codigo'],
            nome=dados_fornecedor['nome']            
        )
        fornecedor.save()
    return render(request, 'fornecedores/cadastroFornecedor.html')

def excluir(request):
    fornecedor = Fornecedor.objects.get()

    fornecedor.delete()
    return redirect('fornecedor:listar')

# Carregar fornecedor para ATUALIZAR
def carregar_fornecedor(request):
    # obter fornecedor baseado no codigo informado
    fornecedor = Fornecedor.objects.get()
    contexto ={
        'fornecedor':fornecedor,
    }
    return render(request, 'fornecedores/atualizarFornecedor.html', context=contexto)

# Atualizar a base de dados 
def atualizar(request):
    if request.method == 'POST':
        form = FornecedorAtualizarForm(request.POST)
        if form.is_valid():
            dados_fornecedor = form.cleaned_data
            fornecedor = dados_fornecedor['codigo']
            fornecedor.nome = dados_fornecedor['nome']          
            fornecedor.save()
        # Apresenta no console os erros 
        else:
            print(form.errors)
    return redirect('fornecedor:listar')
    