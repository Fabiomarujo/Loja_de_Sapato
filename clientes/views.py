from django.shortcuts import render, redirect
from clientes.forms import ClientesForm, ClientesAtualizarForm
from clientes.models import Clientes

def listar(request):
    listar_clientes = Clientes.objects.all()
    contexto = {
        'clientes': listar_clientes,
    }
    return render(request, 'clientes/listarClientes.html', context=contexto)

def cadastro(request):
    return render(request, 'clientes/cadastroClientes.html')

def cadastrar(request):
    form = ClientesForm(request.POST)
    if form.is_valid():
        dados_clientes = form.cleaned_data       
        clientes = Clientes(
            id=dados_clientes['id'],
            cpf=dados_clientes['cpf'],
            nome=dados_clientes['nome'],
            endereco=dados_clientes['endereco'],
            telefone=dados_clientes['telefone'],
            uf=dados_clientes['uf'],
            cidade=dados_clientes['cidade'],
            genero=dados_clientes['genero'],
            contato=dados_clientes['contato'],
            email=dados_clientes['email'],
            senha=dados_clientes['senha'],
        )
        clientes.save()
    return render(request, 'clientes/cadastroClientes.html')

def excluir(request):
    clientes = Clientes.objects.get()

    clientes.delete()
    return redirect('clientes:listar')

# Carregar clientes para ATUALIZAR
def carregar_clientes(request):
    # obter cliente baseado no id informado
    clientes = Clientes.objects.get(pk=id)
    contexto ={
        'clientes':clientes,
    }
    return render(request, 'templates/clientes/atualizarClientes.html', context=contexto)

# Atualizar a base de dados
def atualizar(request):
    if request.method == 'POST':
        form = ClientesAtualizarForm(request.POST)
        if form.is_valid():
            dados_clientes = form.cleaned_data
            clientes = Clientes.objects.get(pk=id)
            clientes.cpf = dados_clientes['cpf']
            clientes.nome = dados_clientes['nome']
            clientes.endereco = dados_clientes['endereco']
            clientes.telefone = dados_clientes['telefone']
            clientes.uf = dados_clientes['uf']
            clientes.cidade = dados_clientes['cidade']
            clientes.genero = dados_clientes['genero']
            clientes.contato = dados_clientes['contato']
            clientes.email = dados_clientes['email']
            clientes.senha = dados_clientes['senha']
            clientes.save()
        # Apresenta no console os erros 
        else:
            print(form.errors)
    return redirect('clientes:listar')
    