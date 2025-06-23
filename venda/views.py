from django.shortcuts import render, redirect
from venda.forms import VendaForm, VendaAtualizarForm
from venda.models import Venda

def listar(request):
    listar_venda = Venda.objects.all()
    contexto = {
        'venda': listar_venda,
    }
    return render(request, 'venda/listarVenda.html', context=contexto)

def cadastro(request):
    return render(request, 'venda/cadastroVenda.html')

def cadastrar(request):
    form = VendaForm(request.POST)
    if form.is_valid():
        dados_venda = form.cleaned_data       
        venda = Venda(
            numero=dados_venda['numero'],
            valor_venda=dados_venda['valor_venda'],
            cliente_cpf=dados_venda['cliente_cpf'],
            venda_numero=dados_venda['venda_numero'],
            produto_codigo=dados_venda['produto_codigo'],
            quantidade=dados_venda['quantidade'],
            preco_venda=dados_venda['preco_venda']            
        )
        venda.save()
    return render(request, 'templates/venda/cadastroVenda.html')

def excluir(request):
    venda = Venda.objects.get()

    venda.delete()
    return redirect('venda:listar')

# Carregar fornecedor para ATUALIZAR
def carregar_venda(request):
    # obter fornecedor baseado no codigo informado
    venda = Venda.objects.get()
    contexto ={
        'venda':venda,
    }
    return render(request, 'venda/atualizarVenda.html', context=contexto)

# Atualizar a base de dados 
def atualizar(request):
    if request.method == 'POST':
        form = VendaAtualizarForm(request.POST)
        if form.is_valid():
            dados_venda = form.cleaned_data
            venda = dados_venda['numero']
            venda.data_venda = dados_venda['data_venda']
            venda.valor_venda = dados_venda['valor_venda']
            venda.cliente_cpf = dados_venda['cliente_cpf']
            venda.venda_numero = dados_venda['venda_numero']
            venda.produto_codigo = dados_venda['produto_codigo']
            venda.quantidade = dados_venda['quantidade']
            venda.preco_venda = dados_venda['preco_venda']          
            venda.save()
        # Apresenta no console os erros 
        else:
            print(form.errors)
    return redirect('venda:listar')
    