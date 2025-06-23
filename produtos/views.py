from django.shortcuts import render, redirect
from produto.forms import ProdutoForm, ProdutoAtualizarForm
from produto.models import Produto

def listar(request):
    listar_produto = Produto.objects.all()
    contexto = {
        'produto': listar_produto,
    }
    return render(request, 'produtos/listarProduto.html', context=contexto)

def cadastro(request):
    return render(request, 'produtos/cadastroProduto.html')

def cadastrar(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        dados_produto = form.cleaned_data       
        produto = Produto(
            codigo=dados_produto['codigo'],
            nome=dados_produto['nome'],
            preco_compra=dados_produto['preco_compra'],
            preco_venda=dados_produto['preco_venda'],
            cor=dados_produto['cor'], 
            tamanho=dados_produto['tamanho'],
            imagem=dados_produto['imagem'],    
            fornecedor_codigo=dados_produto['fornecedor_codigo'],       
        )
        produto.save()
    return render(request, 'produtos/cadastroProduto.html')

def excluir(request):
    produto = Produto.objects.get()

    produto.delete()
    return redirect('produto:listar')

# Carregar produto para ATUALIZAR
def carregar_produto(request):
    # obter produtor baseado no codigo informado
    produto = Produto.objects.get()
    contexto ={
        'produto':produto,
    }
    return render(request, 'produto/atualizarProduto.html', context=contexto)

# Atualizar a base de dados 
def atualizar(request):
    if request.method == 'POST':
        form = ProdutoAtualizarForm(request.POST)
        if form.is_valid():
            dados_produto = form.cleaned_data
            produto = dados_produto['codigo']
            produto.nome = dados_produto['nome']
            produto.preco_compra = dados_produto['preco_compra']
            produto.preco_venda = dados_produto['preco_venda']
            produto.cor = dados_produto['cor']
            produto.tamanho = dados_produto['tamanho']
            produto.imagem = dados_produto['imagem']  
            produto.fornecedor_codigo = dados_produto['fornecedor_codigo']        
            produto.save()
        # Apresenta no console os erros 
        else:
            print(form.errors)
    return redirect('produto:listar')