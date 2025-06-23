from django import forms

# Class formulário para iniciado

class ClientesForm(forms.Form):
    cpf = forms.CharField(max_length=11, help_text='Digite o CPF')
    nome = forms.CharField(max_length=70, help_text='Digite o Nome do Aluno')
    endereco = forms.CharField(max_length=100, help_text='Digite o endereço')
    telefone = forms.CharField(max_length=11, help_text='Digite o número de telefone')
    uf = forms.CharField(max_length=2, help_text='Escolha seu estado')
    cidade = forms.CharField(max_length=50, help_text='Digite sua cidade')
    genero = forms.CharField(max_length=1, help_text='Escolha seu gênero')
    contato = forms.CharField(max_length=100, help_text='Escolha forma de contato')
    email_cliente = forms.CharField(max_length=100, help_text='Digite seu e-mail')
    senha = forms.CharField(max_length=256, help_text='Informe a senha')
    
class ClientesAtualizarForm(forms.Form):
    id = forms.IntgerField(required=True, help_text='Identificação do Cliente')
    cpf = forms.CharField(max_length=11, help_text='Digite o CPF')
    nome = forms.CharField(max_length=70, help_text='Digite o Nome do Aluno')
    endereco = forms.CharField(max_length=100, help_text='Digite o endereço')
    telefone = forms.CharField(max_length=11, help_text='Digite o número de telefone')
    uf = forms.CharField(max_length=2, help_text='Escolha seu estado')
    cidade = forms.CharField(max_length=50, help_text='Digite sua cidade')
    genero = forms.CharField(max_length=1, help_text='Escolha seu gênero')
    contato = forms.CharField(max_length=100, help_text='Escolha forma de contato')
    email_cliente = forms.CharField(max_length=100, help_text='Digite seu e-mail')
    senha = forms.CharField(max_length=256, help_text='Informe a senha')